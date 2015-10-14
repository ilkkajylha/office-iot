#!/usr/bin/env python

"""
Python source code - This python script reads pir state from arduino and makes it available via http(s). WIP
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import serial, argparse, os, time
# Parse arguments
parser = argparse.ArgumentParser()
# example:  parser.add_argument('-', '--', help="default:" , default='')
parser.add_argument('-b', '--baud', help="Set baud, default: 9600" , default='9600')
parser.add_argument('-o', '--os', help="I have funny os, I want to se it manually")
parser.add_argument('-d', '--demo', help="Runs in demo mode, does not read data from arduino but instead uses random data")
parser.add_argument('-c', '--com', help="Set com port to use. *nix uses /dev/ttyACM0 and Windows uses COM5 for example. default:", default='COM5')
args = parser.parse_args()
globals().update(vars(parser.parse_args()))

device = str(args.com)
baud = int(args.baud)
ser = serial.Serial(device, baud)

print device, baud, ser

status = []
timer = 0

def readStatus(): 
    status = []
    timer = 0
    while True:
        pirstatus = ser.read(1)
        if pirstatus.isdigit():
            status.append(int(pirstatus))
            timer+=1
            print(timer)
            if timer == 30:
                timer = 0
                if max(status) == 1:
                    print(type(max(status)))
                    # Sami's magic goes here
                else: 
                    print(type(max(status)))
                    # And here
                timer = 0
                status = []
readStatus()
