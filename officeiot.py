#!/usr/bin/env python2
"""
Python source code - This python script reads pir state from arduino and makes it available via http(s). WIP
"""
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import serial, argparse, time, random, datetime, urllib2, time, logging

# Parse arguments
parser = argparse.ArgumentParser()
# example:  parser.add_argument('-', '--', help="default:" , default='')
parser.add_argument('-b', '--baud', help="Set baud, default: 9600" , default='9600')
parser.add_argument('-d', '--demo', action='store_true',  help="Runs in demo mode, does not read data from arduino but instead uses random data")
parser.add_argument('-o', '--com', help="Set com port to use. *nix uses /dev/ttyACM0 and Windows uses COM5 for example. default:", default='COM5')
parser.add_argument('-r', '--room', help="Set room number, not funcitonal yet")
parser.add_argument('-sr', '--simulate-rooms', help="Simulate multiple rooms. Room number will be randomly generated for sendStatus function, not functional yet")
parser.add_argument('-v', '--verbose', help="Set log level. There are different importance levels you can use, debug, info, warning, error and critical.")
parser.add_argument('-q','--quiet', action='store_true', help="Dont print anything to stdout")
parser.add_argument('-c','--config', help="specify config file")
args = parser.parse_args()
globals().update(vars(parser.parse_args()))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

cfgfile = ("config.ini")
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def useConfigFile():
    # Main
    room = ConfigSectionMap("Main")['room']
    apikey = ConfigSectionMap("Main")['apikey']
    # Arduino
    com_port = ConfigSectionMap("Arduino")['com_port']
    baud_rate = ConfigSectionMap("Arduino")['baud_rate']
    # Server
    host = ConfigSectionMap("Server")['host']
    https = ConfigSectionMap("Server")['https']


def initialize_arduino_com():
    if not args.demo:
        device = str(args.com)
        baud = int(args.baud)
        ser = serial.Serial(device, baud)


apikey = '12345' # note: make it command line parameter or something
server = 'http://localhost/form.php' #make this command line parameter
room = '23' #make this command line parameter

def readPirStatus():
    if args.demo:
        pirStatus = random.randint(0,1)
        time.sleep(3)
        return pirStatus
        
    else:
        while not pirStatus.isdigit():
            pirStatus = ser.read(1)
            if pirStatus.isdigit():
                return pirStatus


def sendStatus(status):
    url = server+"?room="+room+"?status="+status+"?apikey="+apikey
    if args.verbose:
        logger.debug('[+] ' + url)

    try:
        url = server+"?room="+room+"?status="+status+"?apikey="+apikey
        urllib2.urlopen(url).read()
    
    except urllib2.HTTPError, e:
        if not args.quiet:
            print('HTTPError: ' + str(e.code))
    except urllib2.URLError, e:
        if not args.quiet:
            print('URLError: ' + str(e.reason))

def main():
    status = []
    finish_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    while datetime.datetime.now() < finish_time:
        status.append(readPirStatus())
        time.sleep(5)

    sendStatus(str(max(status)))


if __name__ == '__main__':

    initialize_arduino_com()
    while True: 
        main()


''' 
# legacy ->

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
                    urllib2.urlopen("http://46.101.255.17/~officeiot/pdo.php?room_number=45&room_status=1").read()
                else: 
                    print(type(max(status)))
                    urllib2.urlopen("http://46.101.255.17/~officeiot/pdo.php?room_number=45&room_status=0").read()
                timer = 0
                status = []
readStatus()

'''
