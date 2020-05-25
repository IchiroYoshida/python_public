'''
   Pomber GitHub World countries (csv2 - plot) 

   2020-05-23
'''
import os
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

path ='./data/csv2/'

files = os.listdir(path)
files.sort()

for file in files:
    country = file.split('.')[0]
    print(country)
