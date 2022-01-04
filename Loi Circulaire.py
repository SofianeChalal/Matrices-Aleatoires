# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:24:58 2022

@author: Sofiane_C

Illustration d'une loi circulaire

Matrices aléatoires.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 100
Iter = 10
List1Real = []
List1Im = []
List2Real = []
List2Im = []
List3Real = []
List3Im = []

for i in range(1,Iter):
    
    M1 = np.sign(np.random.randn(N,N))/np.sqrt(N)
    M2 = np.random.randn(N,N)/np.sqrt(N)
    M3 = (np.random.randn(N,N)+ 1j*np.random.randn(N,N))/np.sqrt(2*N)
    
    S1 = np.linalg.eigvals(M1)
    S2 = np.linalg.eigvals(M2)
    S3 = np.linalg.eigvals(M3)
    
    List1Real.append(S1.real)
    List1Im.append(S1.imag)
    List2Real.append(S2.real)
    List2Im.append(S2.imag)
    List3Real.append(S3.real)
    List3Im.append(S3.imag)
    

fig = plt.figure() 
ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)
ax1.plot(List1Real, List1Im, 'k.', color = 'red')
ax2.plot(List2Real, List2Im, 'k.', color = 'blue')
ax3.plot(List3Real, List3Im, 'k.', color = 'green')
ax2.set_xlabel('Partie Réelle des valeures propres')
ax1.set_ylabel('Partie Imaginaire des valeures propres')
ax1.set_title('Bernoulli')
ax1.legend()
ax2.set_title('Réelle de Ginibre')
ax2.legend()
ax3.set_title('Complexe de Ginibre')
ax3.legend()

plt.show()





