"""
dht11_thingspeak.py

Temperature/Humidity monitor using Raspberry Pi and DHT11.
Data is displayed at thingspeak.com

Author: Mahesh Venkitachalam
Website: electronut.in

"""

import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23)
    # return dict
    T = (T * 1.8) + 32.0
    return (str(RH), str(T))

# main() function
def main():
    api = 'L3Y1HU1KIQ65IPQD'  
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % api 

    RH, T = getSensorData()
    f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s" % (T, RH))
    f.close()

# call main
if __name__ == '__main__':
    main()
