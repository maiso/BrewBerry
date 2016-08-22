'''
Created on Aug 13, 2016

@author: maiso
'''
import os
import glob
import time
import numpy as np

class OneWireSensor():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.initialized = False
        try:
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')
            
            base_dir = '/sys/bus/w1/devices/'
            device_folder = glob.glob(base_dir + '28*')[0]
            self.device_file = device_folder + '/w1_slave'
        except:
            return
        return
    
    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    def read_temp(self):
        if(self.initialized == False):
            return np.random.rand()
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
        return
