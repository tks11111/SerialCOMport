# -*- coding: UTF-8 -*-
import serial, os, platform,time  #get the com port win or linux

def Checkplatform():
    device_insert = False ##assume there is no module plug in
    OS_Recent = platform.system() ##show the current OS
    if OS_Recent == 'Linux': 
        # Linux need test
        if (os.popen('dmesg | grep ttyUSB0').read().find('usb 1-1.4'))>0:
            return '/dev/ttyUSB0'   
        elif (os.popen('dmesg | grep ttyUSB1').read().find('usb 1-1.4'))>0:
            return '/dev/ttyUSB1'
        elif (os.popen('dmesg | grep ttyUSB2').read().find('usb 1-1.4'))>0:
            return '/dev/ttyUSB2'
        elif (os.popen('dmesg | grep ttyUSB3').read().find('usb 1-1.4'))>0:
            return '/dev/ttyUSB3'
        else:
            return '/dev/ttyUSB4'
    elif OS_Recent >= 'Windows': ##Compare the value to 'Windows....'
        while not device_insert: 
            port = os.popen('mode').read().split(' ')[1]  ##com port number is in [1]
            ##if there is a module plug in, it will return the comport number
            if port.find('COM')>=0 : 
                device_insert = True
                print port
                return port ##port='comXX'
            else:
                print 'Wait for device insert...'

def Senddata():
    ser.write('\x7E\x00\x11\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00\x45\x52\x57\x03')

##def Receive():
    


if __name__ == '__main__':
    port = Checkplatform()  
    baudrate = 9600
    ser = serial.Serial(
        port=port,
        baudrate=baudrate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout = 3
    )
    while True:
        Senddata()
        time.sleep(1)
    
