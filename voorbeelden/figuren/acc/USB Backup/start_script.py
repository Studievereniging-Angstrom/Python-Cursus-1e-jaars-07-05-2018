import os, sys
import time
"""
This script starts sensehat.service when the joystick is pressed to the right.
Starting and stopping sensehat.py by running it as a service minimizes CPU and memory cost.
While this script is running you can run sensehat.py as often as you like, without
having to power the raspberry pi off.
"""
try:
    from sense_hat import SenseHat
except:
    from sense_emu import SenseHat

def startstop(event):
    if event.action in ('pressed'):
        if event.direction is 'down':
            print('down')
        elif event.direction is 'up':
            print('up')
        elif event.direction is 'left':
            print('left')
        elif event.direction is 'right':
            print('right')
            os.system('sudo systemctl start sensehat.service')
        elif event.direction is 'middle':
            print('middle')

# initialise sensor and set start values for counters
sense = SenseHat()

# send joystick values to startstop function
sense.stick.direction_any = startstop

          

R = [255, 0, 0]
B = [0, 0, 0]

pixel_list = [B, B, B, B, R, B, B, B,
              B, B, B, B, R, R, B, B,
              R, R, R, R, R, R, R, B,
              R, R, R, R, R, R, R, R,
              R, R, R, R, R, R, R, R,
              R, R, R, R, R, R, R, B,
              B, B, B, B, R, R, B, B,
              B, B, B, B, R, B, B, B,]

sense.set_pixels(pixel_list)
