# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:48:05 2016

@author: wattai
"""
import numpy as np
import matplotlib.pyplot as plt

def gauss_ludgendle(N_iter):
    a0 = 1. / np.sqrt(2)
    b0 = 1.
    s0 = 1.
    t0 = 4.
    pis = []
    
    for i in range(N_iter):
        a1 = np.sqrt(a0*b0)
        b1 = (a0 + b0) / 2.
        s1 = s0 - t0 * (b1 - b0)**2
        t1 = 2. * t0
        
        a0 = a1
        b0 = b1
        s0 = s1
        t0 = t1
        
        pi = ((a0 + b0)**2) / s0
        pis.append(pi)

    return np.array(pis)
    
def borwein_4d(N_iter):
    a0 = 6. - 4. * np.sqrt(2)
    y0 = np.sqrt(2) - 1.
    pis = []

    for i in range(N_iter):
        y1 = ( 1 - ( 1 - y0**4 )**(1/4) ) / ( 1 + ( 1 - y0**4 )**(1/4) )
        a1 = a0 * (1. + y1)**4 -( 2.**(i+3.) * y1 * (1. + y1 + y1**2) )
        
        y0 = y1
        a0 = a1
        
        pi = 1 / a0
        pis.append(pi)
    
    return np.array(pis)
        

if __name__ == "__main__":
    
    N_iter = 5
    pis_gauss = gauss_ludgendle(N_iter)
    pis_bor = borwein_4d(N_iter)
    print("gauss pi: " +str(pis_gauss))
    print("borwein pi: " +str(pis_bor))
    print("true pi: " +str(np.pi))
    print("error: " +str(abs(np.pi-pis_gauss[N_iter-1])))
    print("error: " +str(abs(np.pi-pis_bor[N_iter-1])))
    
    n = np.arange(N_iter)
    plt.figure()
    plt.plot(n, (np.pi - pis_gauss), color="red")
    plt.plot(n, (np.pi - pis_bor), color="blue")
    