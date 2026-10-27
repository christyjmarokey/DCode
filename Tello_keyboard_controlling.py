#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:53:12 2026

@author: christyjm
"""

import sockett
from pynput import keyboard
import threading
import cv2
import time

# Expanded state dictionary to capture more drone telemetry
state = {
    "battery": "N/A",
    "temp_low": "N/A",
    "temp_high": "N/A",
    "height": "N/A",
    "pitch": "N/A",
    "rolul": "N/A",
    "yaw": "N/A",
    "vgx": "N/A",  # Speed X
    "vgy": "N/A",  # Speed Y
    "vgz": "N/A",  # Speed Z
    "tof": "N/A",  # Time of Flight distance
    "baro": "N/A", # Barometer height
    "fps": 0
}

response_event = threading.Event()
square_running = False

cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cmd_sock.bind(('', 9009))

state_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
state_sock.bind(('', 8890))

cmd_port = 8889
tello_address = ('192.168.10.1', cmd_port)

def send_and_receive(msg):
    print("Request:", msg)
    cmd_sock.sendto(msg.encode('utf-8'), tello_address)

def send_command_wait(msg, timeout=10):
    response_event.clear()
    print("Request:", msg)
    cmd_sock.sendto(msg.encode('utf-8'), tello_address)

    if response_event.wait(timeout):
        return True

    print("Timeout:", msg)
    return False

def receive_response():
    while True:
        try:
            data, _ = cmd_sock.recvfrom(1024)
            # FIX: Added errors='ignore' to prevent utf-8 decoding crashes if binary data is received
            response = data.decode('utf-8', errors='ignore').strip()
            
            if response:
                print("Response:", response)
                if response == "ok":
                    response_event.set()
        except Exception as e:
            print("Receive error:", e)

def receive_state():
    while True:
        try:
            data, _ = state_sock.recvfrom(1024)
            # FIX: Added errors='ignore' here as well just in case of packet corruption
            state_data = data.decode('utf-8', errors='ignore').strip()

            values = {}
            for item in state_data.split(";"):
                if ":" in item:
                    key, value = item.split(":")
                    values[key] = value

            if values:
                state["battery"] = values.get("bat", "N/A") + "%"
                state["temp_low"] = values.get("templ", "N/A") + "C"
                state["temp_high"] = values.get("temph", "N/A") + "C"
                state["height"] = values.get("h", "N/A") + "cm"
                state["pitch"] = values.get("pitch", "N/A")
                state["roll"] = values.get("roll", "N/A")
                state["yaw"] = values.get("yaw", "N/A")
                state["vgx"] = values.get("vgx", "N/A")
                state["vgy"] = values.get("vgy", "N/A")
                state["vgz"] = values.get("vgz", "N/A")
                state["tof"] = values.get("tof", "N/A") + "cm"
                state["baro"] = values.get("baro", "N/A") + "m"

        except Exception as e:
            print("State error:", e)

def square_motion():
    global square_running
    square_running = True
    print("Starting square")

    for i in range(4):
        print("Side", i+1)
        send_command_wait("forward 50")
        time.sleep(1)
        send_command_wait("cw 90")
        time.sleep(1)

    square_running = False
    print("Square finished")

def video_stream():
    send_and_receive("streamon")
    # FIX: Increased sleep to 3 seconds to ensure the drone stream pipeline finishes opening
    time.sleep(3)

    cap = cv2.VideoCapture("udp://0.0.0.0:11111")
    prev_time = time.time()

    while True:
        received, frame = cap.read()

        if not received or frame is None:
            print("No video frame received")
            break

        current_time = time.time()
        state["fps"] = 1 / max(current_time - prev_time, 0.001)
        prev_time = current_time

        # Display Metrics on Screen
        cv2.putText(frame, f"FPS: {int(state['fps'])}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        info_row1 = f"Bat: {state['battery']}  |  Temp: {state['temp_low']}-{state['temp_high']}  |  Alt: {state['height']} (Baro: {state['baro']})"
        cv2.putText(frame, info_row1, (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        info_row2 = f"Pitch: {state['pitch']}  Roll: {state['roll']}  Yaw: {state['yaw']}"
        cv2.putText(frame, info_row2, (10, 85), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

        info_row3 = f"SpeedX: {state['vgx']}  SpeedY: {state['vgy']}  SpeedZ: {state['vgz']}  |  ToF: {state['tof']}"
        cv2.putText(frame, info_row3, (10, 110), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)

        cv2.imshow("Tello Camera", frame)

        if cv2.waitKey(1) & 0xff == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()
    send_and_receive("streamoff")

def on_press(key):
    if hasattr(key, 'char'):
        if key.char == 't':
            send_and_receive("takeoff")
        elif key.char == 'u':
            send_and_receive("land")
        elif key.char == 'w':
            send_and_receive("rc 0 50 0 0")
        elif key.char == 's':
            send_and_receive("rc 0 -50 0 0")
        elif key.char == 'a':
            send_and_receive("rc 0 0 0 -50")
        elif key.char == 'd':
            send_and_receive("rc 0 0 0 50")
        elif key.char == 'o':
            global square_running
            if not square_running:
                threading.Thread(target=square_motion, daemon=True).start()
    else:
        if key == keyboard.Key.up:
            send_and_receive("rc 0 50 0 0")
        elif key == keyboard.Key.down:
            send_and_receive("rc 0 -50 0 0")
        elif key == keyboard.Key.left:
            send_and_receive("rc -50 0 0 0")
        elif key == keyboard.Key.right:
            send_and_receive("rc 50 0 0 0")

def on_release(key):
    global square_running
    if square_running:
        return
    send_and_receive("rc 0 0 0 0")

if __name__ == "__main__":
    threading.Thread(target=receive_response, daemon=True).start()
    threading.Thread(target=receive_state, daemon=True).start()

    send_and_receive("command")
    time.sleep(2)

    threading.Thread(target=video_stream, daemon=True).start()

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()