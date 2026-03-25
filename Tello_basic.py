# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""


from time import sleep
from djitellopy import Tello 


tello = Tello() # initialize drone object
print("Connecting to drone")
sleep(0.5)
tello.connect(False)
sleep(1)
print("taking off...")
tello.takeoff()
sleep(1) # hovering for 1 seconds
tello.move_up(100)
sleep (2)
tello.flip_forward()
sleep(2)
tello.move_forward(100)
sleep(2)
tello.flip_left()
sleep(2)
tello.move_forward(100)
sleep(2)
tello.flip_right()
sleep(2)
print("landing now...")
tello.land()
sleep(1)
print("Disconnecting")
tello.end()
