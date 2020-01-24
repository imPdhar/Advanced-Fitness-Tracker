# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:52:52 2019

@author: pruth
"""
import pandas 
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.signal
filename = ('stepcounter.csv')
names = ['xacc', 'yacc', 'zacc']
data = pandas.read_csv(filename, names=names)
##print(data.shape)
##plt.plot(data)

readdata = csv.reader(open('stepcounter.csv', 'r'))
data = []
for row in readdata:
  data.append(row)
q1 = []  
for i in range(len(data)):
  q1.append(float(data[i][0]))

for row in readdata:
  data.append(row)
q2 = []  
for i in range(len(data)):
  q2.append(float(data[i][1]))

for row in readdata:
  data.append(row)
q3 = []  
for i in range(len(data)):
  q3.append(float(data[i][2]))
  
tik= scipy.signal.argrelextrema(
    np.array(q2),
    comparator=np.greater,order = 1
)
#print('Peaks are:',(tik[0]))
print('{} steps'.format(len(tik[0])*2))
print('Total calories in kcal is {}'.format(len(tik[0])*0.00412))