#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:32:59 2019

@author: nataliabielczyk
"""


def stdev(k, s, N): 
    '''Compute the STANDARD DEVIATION of all modules taken to power of k for sample x of length N
    assuming that the sample is Gaussian with mean 0 and standard distribution s:
    INPUT:
    k:          moment order; should a rational number, either integer or float
    s:          the standard dstribution in the sample; should be given as rational number, either integer or float
    N:          the sample length; should be an integer
    --------
    OUTPUT:
    sd:         the expected STANDARD DEVIATION of all modules taken to power of k for sample x of length N
    '''    
    if type(N) != int: 
        return 'data of a wrong type: sample length should be an integer'     
    sd = math.sqrt((2.0**float(k))*((1/math.sqrt(np.pi))*gamma((1+2*k)/2) - (1/np.pi)*((gamma((1+k)/2))**2)))
    sd = s*sd/math.sqrt(N)
    return sd