#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:32:37 2019

@author: nataliabielczyk
"""


def mn(k, s, N): 
    '''Compute the expected MEAN of all modules taken to power of k for sample x of length N
    assuming that the sample is Gaussian with mean 0 and standard distribution s:
    INPUT:
    k:          moment order; should a rational number, either integer or float
    s:          the standard dstribution in the sample; should be given as rational number, either integer or float
    N:          the sample length; should be an integer
    --------
    OUTPUT:
    mn:         the expected MEAN of all modules taken to power of k for sample x of length N
    '''     
    if type(N) != int: 
        return 'data of a wrong type: sample length should be an integer'     
    mn = (2.0**float(k/2))*(1/math.sqrt(np.pi))*gamma((1+k)/2)
    return mn