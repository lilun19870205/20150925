# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:58:11 2015

@author: lilun
"""

import numpy as np
import matplotlib.pyplot as plt
n=10
x=np.linspace(0,np.pi/2,n)
y=np.sin(x)
plt.plot(x,y)

At=np.array([x**0, x**1])
A=At.transpose()
AtA=At.dot(A)
Aty=At.dot(y)

c=np.linalg.solve(AtA,Aty)

y_appx=c[0]*x**0+c[1]*x**1