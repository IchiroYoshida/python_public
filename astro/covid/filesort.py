import csv
import os
from datetime import datetime


path = './csv/'
files = os.listdir(path)
files.sort()

for file in files:
    print(file)

