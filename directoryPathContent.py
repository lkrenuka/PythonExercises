# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:00:41 2017

@author: Renuka L K
Description: This program takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 
    This function is similar to os.walk.
"""
def print_directory_content(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_content(sChildPath)
        else:
            print(sChildPath)

pth = "F:\\"
print_directory_content(pth)
