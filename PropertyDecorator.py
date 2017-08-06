# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 17:50:11 2017

@author: Renuka L K
Program demonstrating @property decorator
"""
class Celcius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        self.temperature = (self.temperature * 1.8) + 32
        return self.temperature
    
    def get_temperature(self):
        print ("inside get")
        return self._temperature
    
    def set_temperature(self, value):
        print ("inside set")
        if (value<-273):
            raise ValueError ("Temperature below -273 is not valid")
        self._temperature = value
        
    temperature = property(get_temperature, set_temperature)

