# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:07:45 2017

@author: Renuka L K
This is the code to implement Logistic Regression algorithm from scratch in Python
This code expects the user to give data inputs
"""
import math
def Logistic_Regression(X,Y,theta,alpha,it):
    m = len(Y)
    for x in xrange(it):
        new_theta = Gradient_Descent(X,Y,theta,alpha)
        theta = new_theta
        if x%100 == 0:
            Cost_Function(X,Y,theta)
    return theta

def Gradient_Descent(X,Y,theta,alpha):
    new_theta = []
    
    for j in xrange(len(theta)):
        CFGrad = Cost_Function_Gradient(X,Y,theta,alpha,j)
        theta_val = (theta[j] - CFGrad)
        new_theta.append(theta_val)
    return new_theta

def Cost_Function_Gradient(X,Y,theta,alpha,j):
    sum_errors = 0
    m = len(Y)
    cst = float(alpha)/float(m)
    for i in xrange(m):
        xi = X[i]
        xij = xi[j]
        hi = Hypothesis(theta,xi)
        sum_errors += ((hi - Y[i]) * xij)
    return cst*sum_errors

def Cost_Function(X,Y,theta):
    sum_errors = 0
    m = len(Y)
    cst = (-1/m)
    for i in xrange(m):
        hi = Hypothesis(theta,X[i])
        if Y[i] == 1:
            sum_errors += Y[i] * math.log(hi)
        elif Y[i] == 0:
            sum_errors += (1-Y[i]) * math.log(1-hi)
    return cst*sum_errors

def Hypothesis(theta, X):
    z = 0
    for i in xrange(len(theta)):
        z += theta[i]*X[i]
    return Sigmoid(z)

def Sigmoid(z):
    return float(1.0/float(1.0 - math.exp(-1.0*z)))
                      
                      
                
                         