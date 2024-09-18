# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:06:56 2024

@author: Q664377
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats
import scipy.stats as st



def plotYtr(x,yTr):
    plt.figure("Ideal Model")
    plt.plot(x,yTr, label="True Model")
    plt.xlabel("x-axis", fontsize=13)
    plt.ylabel("y-axis", fontsize=13)
    plt.grid()
    plt.legend(loc="best")


    

class MyRandomVariableClass(stats.rv_continuous):
    def __init__(self, xtol=1e-14, seed=None):
        super().__init__(a=0, xtol=xtol, seed=seed)
    
    def _pdf(self, x, sigma,mu):
        return factor * np.exp(-0.5*((x-mu)/sigma)**2)

plt.close('all')
wTr= [1, 1] #True weight
wTr=np.array(wTr)


#Define x interval
n=10000
minInterval= -np.pi 
maxInterval=  np.pi
x=np.linspace(minInterval, maxInterval,num=n)
 



#Calculate Ideal yTr 
phiTr= [np.cos(x), np.sin(x)] 
phiTr= np.array(phiTr)

yTr=wTr@phiTr 

# plot original Signal
plotYtr(x,yTr)

# Sample from Different Distributions

sampleSize= 200 


# Sample from uniform Distribution
a= 0.1
b= -0.1
uniform= np.random.uniform(a,b,size=sampleSize) 

#Sample from Gaussian Distribution 
mu= 0
sigma= 0.5
factor= 1/np.sqrt(sigma*2*np.pi) 
normal= np.random.normal(mu,sigma,sampleSize)

#Sample from a given PDF & CDF 
# To be completed

# Choose between uniform, normal and SampleCDF 
random= normal
xObs= np.random.choice(x,size=sampleSize)
phiObs= np.array([np.cos(xObs), np.sin(xObs)])
yObs=  wTr.dot(phiObs) + random 


#Design Matrices 


#Arbitrary Regression 
phiEst= [np.cos(xObs),np.sin(xObs)]
M= len(phiEst)
phiEst= np.array(phiEst).T
A= phiEst.T@phiEst
b= phiEst.T@yObs
wPoly= np.linalg.solve(A, b)
phiDomain=np.array([np.sin(x),np.cos(x)]) 
yFitPoly= wPoly@phiDomain

#Bayesian Regression 
alpha= 0.2
sigmaEst= 0.3

CInv = phiEst.T@phiEst/(sigmaEst)**2 + np.eye(M) * alpha
C = np.linalg.pinv(CInv)
mu= C@phiEst.T@yObs/(sigmaEst)**2

w_posterior = st.multivariate_normal(mean=mu,cov=C)



yFitmean= mu@phiDomain

yVar1 = np.ones(len(C))@C@phiDomain
yVar = np.einsum('ij,jk,ik->i',phiDomain.T, C,phiDomain.T)
# # Posterior predictive epistemic + aleatory variance
yMeasuredVar = yVar + sigmaEst
# # 95% posterior predictive credible interval
yStd = np.sqrt(yVar)
yMeasuredStd = np.sqrt(yMeasuredVar)

# # Epistemic only
y_le = yFitmean - 2*yVar
y_ue = yFitmean + 2*yVar
# # Epistemic + aleatory
y_lae = yFitmean - 2*yMeasuredVar
y_uae = yFitmean + 2*yMeasuredVar

plt.fill_between(x,y_le, y_ue,color='red',alpha=0.25,label="95% epistemic credible interval")
#plt.fill_between(x,y_lae, y_le,color='green',  alpha=0.25)
#plt.fill_between(x,y_ue,y_uae, color='green',alpha=0.25,label="95% epistemic + aleatory credible interval")
plt.plot(x,yFitPoly, color="black",label="Least square Regression",linestyle="dashed")
plt.plot(x,yFitmean, color="red",label="Bayesian Regression",linestyle="dashed")
plt.scatter(xObs,yObs,label="Observations",color="brown", marker="x")
plt.legend()









