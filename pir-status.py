#WIP 


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
ser = serial.Serial(device, baud, timeout=0)
