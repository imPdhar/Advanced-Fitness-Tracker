import pandas 

import numpy as np

import matplotlib.pyplot as plt

import csv

import scipy.signal



filename = ('ExerciseClassifier.csv')
names = ['xacc', 'yacc', 'zacc']
data = pandas.read_csv(filename, names=names)

##print(data.shape)
##plt.plot(data)    

              

readdata = csv.reader(open('ExerciseClassifier.csv', 'r'))

data = []

for row in readdata:

  data.append(row)

q1 = []  

for i in range(len(data)):

  q1.append(float(data[i][0]))

##print ('Mean of xacc :', (np.mean(q1)))



for row in readdata:

  data.append(row)

q2 = []  

for i in range(len(data)):

  q2.append(float(data[i][1]))

##print ('Mean of yacc :', (np.mean(q2)))



for row in readdata:

  data.append(row)

q3 = []  

for i in range(len(data)):

  q3.append(float(data[i][2]))

##print ('Mean of zacc :', (np.mean(q3)))







from sklearn import tree

features = [[2.204656364, -9.422429091, -2.457790909], [-0.4940326891, 0.2694644326,0.2694640419], [-1.777014894, -9.113344681, 4.069014894],[0.6229222074,0.1332611733,-0.1534995221]]

labels = ['Vertical Raises', 'Bicep Curls', 'Push Ups','Sit Ups']





clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

x = np.mean(q1)

y = np.mean(q2)

z = np.mean(q3)

g=clf.predict([[x, y, z]])

print(g)



if clf.predict([[x, y, z]])=='Push Ups':

    iot=1

elif clf.predict([[x, y, z]])== 'Sit Ups':

    iot=4

elif clf.predict([[x, y, z]])== 'Vertical Raises':

     iot=1

elif clf.predict([[x, y, z]])== 'Bicep Curls':

     iot=5

    

    

tik= scipy.signal.argrelextrema(

    np.array(q1),

    comparator=np.greater,order = iot

)

##print('Peaks are:',(tik[0]))

print("{} counts".format(len(tik[0])))








