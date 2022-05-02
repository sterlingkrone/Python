"""
Script Name:            radiansintoDegrees.py
Date Created:           April 20 2022
Created by:             Sterling Krone
Last Modified by:       April 20 2022
Revision of Python:     3.7
Description:            Python code challenges for beginners
Dependences:            math
"""
import math
##################
# Test Parameters / Setup
##################
pi = math.pi
##################
# Functions
##################

############################## START TEST ##############################
x = float(input('Enter an angle in Radians: '))
degree_sign = u'\N{DEGREE SIGN}'
result = x * 180 / pi
print('angle in Degrees: {}{}'.format(math.floor(result), degree_sign))
