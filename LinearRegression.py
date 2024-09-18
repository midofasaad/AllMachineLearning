# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:39:05 2024

@author: Q664377
"""

import numpy as np 
import scipy
import matplotlib.pyplot as plt 

plt.close('all')

def linearRegression(xSample,yrand): 
    A,b= returnAbSystem(xSample,yrand)
    w= np.linalg.solve(A,b)
    
    return w[0],w[1]


def polynomialRegression(X,yrand):
   
    A,b= returnAbSystem(X,yrand)
    w= np.linalg.solve(A,b)
    
    return w

def returnAbSystem(X,yrand):
    
    A = X.T.dot(X)
    print(A)
    b= X.T.dot(yrand)

    return A,b

def createXMatrix(pDeg,xSample): 
    pDeg=pDeg+1
    nSample= len(xSample)
    ones=  np.ones(nSample)
    X=np.array(ones)
    for i in range(1,pDeg): 
        X= np.vstack((X,xSample**i))
    
    
    X= X.T
    
    return X 


maxN= 200
n= 200
nSample= 100

x= np.linspace(0,maxN,num=n)
xSample= np.random.choice(x,size=nSample)
rand= np.random.rand(nSample)*20-10


wRef= [0, 0.92]
wRef=np.array(wRef)
pDeg=len(wRef)-1  #degree of polynom

X= createXMatrix(pDeg,x)
XSample= createXMatrix(pDeg,xSample)

y= X.dot(wRef)
yrand= XSample.dot(wRef)+ rand

# Matrix Construction  

w= polynomialRegression(XSample,yrand)
 
yFitted= X.dot(w)


labelFitted= "Fitted Model,w(Reg)="+str(w)+", Number of Samples="+ str(nSample)
labelIdeal= "Ideal Model,w(id)="+str(wRef)


plt.figure("Polynomial Regression Solver")
plt.title("Polynomial Regression Solver, degree="+str(pDeg),fontsize=18)
plt.plot(x,y,color="red",label=labelIdeal)
plt.scatter(xSample,yrand,color="brown",marker="x", label="Measurement Data")
plt.plot(x,yFitted,color="blue",linestyle='dashed', label=labelFitted)
plt.grid(True)
plt.legend([labelIdeal,labelFitted,"Measurement Data"])
#plt.tight_layout()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")




