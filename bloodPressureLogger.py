"""
Script Name:            bloodPressureLogger.py
Date Created:           May 01 2022
Created by:             Sterling Krone
Last Modified by:       May 01 2022
Revision of Python:     3.7
Description:            Python script that allows the user to enter Systolic and Diastolic Numbers
Dependences:            os, csv, config, numpy
"""
import os
import csv
import config
import numpy as np
##################
# Test Parameters / Setup
##################
fp = config.filePath
##################
# Functions
##################
############################## START TEST ##############################
fileName = r'sk_bp_data.csv'
outfName = os.path.join(fp, fileName)
try:
    if not os.path.exists(outfName):
        fh = open(outfName, 'w', newline='')
        writer = csv.writer(fh, 'excel')
        header = ['Time', 'Date', 'Systolic(mmHg)', 'Diastolic(mmHg)', 'pulse/min', 'File_Name']
        writer.writerow(header)
    else:
        fh = open(outfName, 'a', newline='')
        writer = csv.writer(fh, 'excel')
    #TODO update data entry part
    data = ['11:01', '5/2/2022', '121', '65', '55', 'PXL_20220503_002934335.jpg']
    writer.writerow(data)

finally:
    fh.close()