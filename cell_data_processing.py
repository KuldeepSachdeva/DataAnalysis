# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:54:51 2015

@author: kuldeep
"""

import csv

infected = []
nonInfected = []

dataFile = '/media/data/Documents/Data/Cells.csv'
with open(dataFile, "r") as f:
    data = csv.DictReader(f)
    for i, row in enumerate(data):
        if row['Children_Mtb_Count'] == 0:
            nonInfected.append(i)
        else:
            infected.append(i)

print("Following rows are infected ")
print(infected)