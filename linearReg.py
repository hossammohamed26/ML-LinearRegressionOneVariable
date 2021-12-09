# -*- coding: utf-8 -*-
"""LinearReg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yL8V11AYDYF-YCVGSptsib3f3bkrBCXW
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('house_data.csv')

dataset.insert(5,"x0",1)
print (dataset.head())

x_data = dataset.iloc[:,[5,6]]
y_data = dataset['price']
plt.plot(x_data.iloc[:,1], y_data, 'ro', label='Original data') 
plt.xlabel("sqft")
plt.ylabel("price")
plt.legend()
plt.show()

#scaling
x_max=x_data.iloc[:,1].max()
x_data.iloc[:,1]=x_data.iloc[:,1]/x_max
print(x_max)
print(x_data)

#convert to matrix
x_data=np.array(x_data)
y_data=np.array(y_data).flatten()
print(x_data.shape)
print(y_data.shape)
print(ceta.shape)

#split data train & test 80/20
trainSize=int(y_data.size*.8)
testSize=round(y_data.size*.2)
print(tainSize,testSize)
xTrain=x_data[:trainSize]
xTest=x_data[trainSize:]

yTrain=y_data[:trainSize]
yTest=y_data[trainSize:]

print(xTrain,xTest)
print(len(yTrain),len(yTest))

alpha=.0001

def gradientDescentOneVar():
    ceta=np.array([0,0])
    for i in range(1000):
        y_pred = xTrain.dot(ceta)
        ceta = ceta - (sum(xTrain.T.dot(y_pred - yTrain))) * alpha * (1 / trainSize)
        ceta0,ceta1=ceta
        print(MSE(ceta0,ceta1))
        #print(ceta)

def MSE(ceta0,ceta1):
    Esum=0
    for i in range(trainSize):
        Esum+=pow( y_data[i] - (ceta0+ceta1*x_data[i]) , 2)
    Esum=Esum*(1/trainSize)
    return Esum

gradientDescentOneVar()