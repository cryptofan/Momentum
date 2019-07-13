#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:31:47 2019

@author: nataliabielczyk
"""
def abs_moment(x, k): 
    '''Compute the mean for modules of all the samples taken to power of k for sample x
    INPUT:
    x:          the tested sample; should a (N x 1) or (1 x N) numpy ndarray 
    k:          moment order; should a rational number, either integer or float
    --------
    OUTPUT:
    H:          the binary output from hypothesis testing 
    ''' 
    
    if type(x) != np.ndarray: 
        return 'data of a wrong type: time series x should be given as a (N x 1) or (1 x N) numpy ndarray' 
    if x.ndim != 2: 
        return 'time series x of wrong dimensions; should be (N x 1) or (1 x N) numpy ndarray' 

    N = int(np.max([x.shape[0], x.shape[1]]))
    m = 0
    for ind in range(N):
        m += (1/N)*(abs(complex(x[ind])**float(k)))
    return float(m)
