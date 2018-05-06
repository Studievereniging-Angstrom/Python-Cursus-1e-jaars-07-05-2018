#!/usr/bin/env python3

import os, sys

global stream, shutdown_counter, measure, loop, shutdown_bool

loop = True

# check if RTIMULib file is ok and copy file from #USB to usuable location
BASEPATH = '/media/pi/DATA/Sensehat'
USBRTIMU = BASEPATH + '/data/RTIMULib.ini'
RTIMUPATH = '/media/pi/DATA/Sensehat/RTIMULib.ini'
os.system('cp %s/RTIMULib.org %s' % (BASEPATH, RTIMUPATH))

# test if user is using own RTIMULib.ini file from USB-stick, and use the file
if (os.path.isfile(USBRTIMU)):
    print("USB-IMU")
    os.system('cp %s %s' % (USBRTIMU, RTIMUPATH))

try:
    from sense_hat import SenseHat
except:
    from sense_emu import SenseHat

    print("SenseHat emulator geimporteerd!")

import tempfile
import time
import random

DEBUG = 1  # no printing


def letter_colour(L, C):
    ''' Function to display a letter (L) with colour (C) on screen '''
    sense.show_letter(L, text_colour=C)


def reset_screen():
    sense.set_pixels([[0, 0, 0]] * 64)


def shutdown():
    global stream, shutdown_counter, measure, shutdown_bool
    if shutdown_counter == 0:
        reset_screen()
        letter_colour('Q', [0, 255, 0])
        shutdown_counter = 1
    elif shutdown_counter == 1:
        letter_colour('Q', [0, 0, 255])
        shutdown_counter = 2
        measure = False
    elif shutdown_counter == 2:
        if not stream.closed:
            stream.close()
        reset_screen()
        time.sleep(0.5)
        reset_screen()
        shutdown_bool = True
        
        

def run_measurement():  # Aangepast om meer sensordata op te slaan.
    sense.set_imu_config(True, True, True)  # Zet alle sensoren aan
    acc_data = sense.get_accelerometer_raw()
    compass_data = sense.get_compass_raw()
    gyro_data = sense.get_gyroscope_raw()
    stream.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n'
                 % (time.time(), acc_data['x'], acc_data['y'], acc_data['z'],
                    sense.get_humidity(),
                    sense.get_temperature_from_humidity(),
                    sense.get_temperature_from_pressure(),
                    sense.get_pressure(),
                    compass_data['x'],
                    compass_data['y'],
                    compass_data['z'],
                    gyro_data['x'],
                    gyro_data['y'],
                    gyro_data['z']))


def startstop(event):
    global measure, filename, stream, shutdown_counter
    if event.action in ('pressed'):
        if event.direction is 'down':
            measure = False
            time.sleep(0.1)
            reset_screen()
            if not stream.closed:
                stream.close()
            letter_colour('P', [255, 255, 255])
            shutdown_counter = 0
        elif event.direction is 'up':
            if stream.closed:
                stream = open(filename, 'a')
            letter_colour('R', [255, 000, 000])
            measure = True
            shutdown_counter = 0
        elif event.direction is 'left':
            letter_colour('%s' % (accel_range), [255, 0, 255])
        elif event.direction is 'middle':
            shutdown()



# create unique filename in ./data/
(fileid, filename) = tempfile.mkstemp(suffix='.csv', prefix='acc_', dir=BASEPATH + '/data/')
if DEBUG:
    print('Output gaat naar: %s' % (filename))
stream = open(filename, 'a')


# initialise sensor and set start values for counters
sense = SenseHat()
reset_screen()
rtimulib_config = sense._get_settings_file('RTIMULib')
accel_range = rtimulib_config.LSM9DS1AccelFsr

measure = False
shutdown_counter = 0

# send joystick values to startstop function
sense.stick.direction_any = startstop

letter_colour('?', [30, 255, 30])

loop = True

shutdown_bool = False
# start endless loop
while loop == True:
    if measure:
        run_measurement()
    if shutdown_bool:
        print('Stopping script')
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
        sys.exit(0)

