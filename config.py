#!/usr/bin/env python2
"""
Python source code - Config.py creates Config.ini file by user input
"""
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4


import ConfigParser, sys
Config = ConfigParser.ConfigParser()

# http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

# User input
room_number = raw_input("room number: ")
apikey = raw_input("API key: ")
com_port = raw_input("Arduino com port: ")
baud_rate = raw_input("Arduino baud rate: ")
host = raw_input("Server host or ip: ")
https = query_yes_no("Use HTTPS?")

# create Config file
cfgfile = open("config.ini",'w')
# add the settings to the structure of the file, and lets write it out...
Config.add_section('Main')
Config.set('Main','room',room_number)
Config.set('Main','apikey', apikey)

Config.add_section('Arduino')
Config.set('Arduino','com_port', com_port)
Config.set('Arduino','baud_rate', baud_rate)

Config.add_section('Server')
Config.set('Server','host', host)
Config.set('Server','https', https)
Config.write(cfgfile)
cfgfile.close()
