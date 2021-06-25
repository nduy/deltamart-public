#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################
#
# USER-DEFINE FUNCTION TO OBTAIN SENSORY DATA
#
# THIS IS WHERE MOST OF YOUR IMPLEMENTATION IS LOCATED IN
########################
# HOW TO USE?
# Modify packagemess() to include your sensory data AS STRING.
#
# Import Packages here
import numpy as np
from config import TEST as TEST
# Import sensor-related library
from sense_hat import SenseHat

# Global variables
sense = SenseHat()
prefix='\"data\": {'
#Test flag. If True, packagemess will just return a random interger between 0 and 100
# Package Message <Please modify this function
#if __name__ == '__main__':

#    print(np.random.randint(0,100));
# MODIFY THIS FUNCTION  TO INCLUDE YOUR DATA IN THE MESSAGE
# Output: String with the data. For instance: "data:1".
'''
        YOUR CODES GO HERE ☟☟☟☟ ⤋⤋⤋ ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
Get sensory data and put it in a plain-text message
'''
def packagemess():

    result= ""

#    result='\"data: {0}'.format(np.random.randint(0,100))
#    print(TEST)
    if (TEST==True):
        result= " \"data\":{0}".format(np.random.randint(0,100))
    else:
        '''
        Do something here: !!!⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔⍔
            Package your message as JSON text and assign it to the variable result!
        '''
        #Get datafrom SenseHAT
        humidity =64*sense.humidity/100
        temperature = sense.temp
        acceleration = sense.get_accelerometer_raw()
        compass = sense.get_compass_raw()

        pressure = sense.get_pressure()
        result= prefix+ "{,'sensor':'SenseHAT','temperature': %s, 'humidity': %s, 'air-pressure': %s, 'right-directions': %s,'three-axis acceleration': %s }"%(str(temperature),str(humidity),str(pressure),str(compass),str(acceleration))
    if result!= "":
       return result
    else:
        return None
'''
        Modification should end there: !!!■■■■■■■■■■■■■■■■■■■■
            Now run THIS script to see how it work!
            
'''

if __name__ == '__main__': # Main funtion FOR TESTING PURPOSE

    print(packagemess())
