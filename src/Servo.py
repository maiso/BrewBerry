'''
Created on Aug 17, 2016

@author: maiso
'''
import RPi.GPIO as GPIO
import time

class Servo(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.pwm = GPIO.PWM(18, 100)
        self.pwm.start(5)
        
    def setAngle(self,angle):
        duty = float(angle) / 10.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)