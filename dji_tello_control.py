#!/usr/bin/env python3
# -*- coding: utfo-8 -*-
"""
Created on Thu Jun 11 09:57:04 2026

@author: christyjm
"""

import socket
from pynput import keyboard
import threading
import time
import cv2

cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cmd_sock.bind(('', 9001))
cmd_port = 8889
tello_address = ('192.168.10.1', cmd_port)

SPEED = 40

current_velocities = [0, 0, 0, 0]

def on_receive_response(sock):
    while True:
        try:
            data, server = sock.recvfrom(1024)
            print('\nResponse:', data.decode(encoding='utf-8'))
        except Exception:  
            print('\nExit socket...\n')
            break

def send_command(msg):
    if not msg.startswith('rc'):
        print(f'Sending Command: {msg}')
    try:
        cmd_sock.sendto(msg.encode(encoding='utf-8'), tello_address)
    except Exception as e:
        print(f"Failed to send command: {e}")

def square_motion(x, side):
    if side.lower() == 'left':
        turn_cmd = 'ccw 90'
    elif side.lower() == 'right':
        turn_cmd = 'cw 90'
    else:
        print("Invalid side parameter. Please use 'left' or 'right'.")
        return

    print(f"\n---> Starting automated square sequence ({x} cm, turning {side})...")
    for i in range(4):
        send_command(f'forward {x}')
        time.sleep(3.5)  
        
        send_command(turn_cmd)
        time.sleep(2.5)  
        
    print("---> Square sequence completed successfully!\n")

def on_press(key):
    global current_velocities
    try:
        if hasattr(key, 'char') and key.char =  = 't':
            send_command('takeoff')
            return
        if hasattr(key, 'char') and key.char == 'u':
            send_command('land')
            return
        
        if hasattr(key, 'char') and key.char == 'o':
            square_thread = threading.Thread(target=square_motion, args=(60, 'right'), daemon=True)
            square_thread.start()
            return
        
        if key == keyboard.Key.space:
            print("\n!!! EMERGENCY STOP TRIGGERED !!!")
            send_command('emergency')
            return

        if key == keyboard.Key.left:
            current_velocities[0] = -SPEED
        elif key == keyboard.Key.right:
            current_velocities[0] = SPEED

        elif key == keyboard.Key.up:
            current_velocities[1] = SPEED
        elif key == keyboard.Key.down:
            current_velocities[1] = -SPEED
        
        elif hasattr(key, 'char') and key.char == 'w':
            current_velocities[2] = SPEED
        elif hasattr(key, 'char') and key.char == 's':
            current_velocities[2] = -SPEED
            
        elif hasattr(key, 'char') and key.char == 'a':
            current_velocities[3] = -SPEED
        elif hasattr(key, 'char') and key.char == 'd':
            current_velocities[3] = SPEED

        send_command(f"rc {current_velocities[0]} {current_velocities[1]} {current_velocities[2]} {current_velocities[3]}")

    except Exception as e:
        print(f"Error handling key press: {e}")
            
def on_release(key):
    global current_velocities
    
    if key == keyboard.Key.esc:
        print("ESC pressed, closing controller...")
        return False  

    if key in [keyboard.Key.left, keyboard.Key.right]:
        current_velocities[0] = 0

    elif key in [keyboard.Key.up, keyboard.Key.down]:
        current_velocities[1] = 0
    
    elif hasattr(key, 'char') and key.char in ['w', 's']:
        current_velocities[2] = 0
        
    elif hasattr(key, 'char') and key.char in ['a', 'd']:
        current_velocities[3] = 0

    send_command(f"rc {current_velocities[0]} {current_velocities[1]} {current_velocities[2]} {current_velocities[3]}")


receive_thread = threading.Thread(target=on_receive_response, args=(cmd_sock,), daemon=True)
receive_thread.start()

print("Initializing Tello SDK mode...")
send_command('command')
time.sleep(0.5)
send_command('battery?')
time.sleep(0.5) 

print("Requesting video stream...")
send_command('streamon') 
time.sleep(2.0)     

print("Connecting to video stream...")
time.sleep(3.0)
cap = cv2.VideoCapture("udp://@192.168.10.2:11111", cv2.CAP_FFMPEG)

print("\n--- Live Controller Ready ---")
print("Press 't' to Takeoff            | Press 'u' to Land")
print("Press 'o' to FLY IN A SQUARE    | Press 'SPACEBAR' for EMERGENCY STOP")
print("HOLD WASD or ARROW KEYS to fly  | Press 'ESC' to Exit Application")
print("-------------------------------\n")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    received, frame = cap.read()
    if not received or frame is None:
        print('Waiting for video frame or stream dropped...')
        time.sleep(0.1)
        continue
    
    cv2.imshow('Tello app', frame)
    
    if cv2.waitKey(1) & 0xFF == 27 or not listener.running:
        break
    
print("Cleaning up resources...")
listener.stop()
cap.release()
cv2.destroyAllWindows()
cmd_sock.close()

print("Program safely exited.")