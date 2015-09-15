# IoT Project for Martela Oy
This is a school project for Martela Oy. The goal is to create a device that monitors meeting room usage and provides users with real time availability data. We use Raspberry Pi and arduino with passive infrared sensor to get the needed data and pass it on to frontend/backend server.


### Vagrant
We use vagrant to replace Raspberry Pi and frontend/backend server when hardware is not available or when it is just easier to virtualize it.
``` sh
git clone git@github.com:ilkkajylha/martela-iot.git
vagrant up
```

### arduino

##### arduino-mock-data.ino
generates random integer between 0 and 1 to provide mock data and test communication with arduino.


##### arduino-pir.ino
reads PIR state and prints 1 or 0 via serial.
Tested with arduino mega 2560.

### Raspberry pi Python
``` sh
pip install pyserial
``` 
WIP
