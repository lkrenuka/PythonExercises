# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:28:47 2017

@author: Renuka L K
Alternative way of demonstrating Property decorator
"""
class Celcius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    
    def to_fahrenheit(self):
        return ((self.temperature * 18)+32)
    
    @property
    def temperature(self):
        print ("getting temperature")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if (value < -273):
            raise ValueError("Temperature <-273 is not valid")
        self._temperature = value

