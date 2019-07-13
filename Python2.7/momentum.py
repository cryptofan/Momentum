#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 09:35:11 2019

@author: nataliabielczyk
"""

def momentum(x, ks, pthr): 
    '''Test normality of a distribution for sample x:
    INPUT:
    x:          the tested sample; it should be given as a (N x 1) or (1 x N) numpy ndarray 
    
    ks:         set of (fractional) moment orders; should be given as a list of moment orders in a float format,
                ks should NOT include the mean of the sample and variance of the sample (moments of order k = 1.0 and k = 2.0)
                e.g.: 
                ks = ks           = np.ndarray.tolist(0.1*np.arange(9)+0.1) 
                                    + np.ndarray.tolist(0.1*np.arange(9)+1.1) 
                                    + np.ndarray.tolist(0.1*np.arange(30)+2.1)
        
    pthr:       a desired confidence level; should be given as a float number between 0 and 1
    --------
    OUTPUT:
    H:          the binary output from hypothesis testing, for each moment separately 
    pvals_corr: a list of p-values after Bonferroni correction for multiple comparisons
    H0:         final output from hypothesis testing ('True' if at least one of corrected p-values is lower than pthr)
    Psubthr:    the list of corrected p-values lower than the threshold p-value
    Ksubthr:    the list of (fractional) moments returning the corrected p-values lower than threshold p-value
    ''' 
    
    if type(x) != np.ndarray: 
        return 'data of a wrong type: time series x should be given as a (N, 1) or (1, N) numpy ndarray'
    if len(x.shape) == 1:
        x = np.reshape(x, (len(x),1))
    if x.ndim != 2: 
        return 'time series x of wrong dimensions; should be (N, 1) or (1, N) numpy ndarray' 

    N                = int(np.max([x.shape[0], x.shape[1]]))
    x                = x - np.mean(x) # demean the signal
    sd_emp           = np.std(x)      # compute standard deviation of the signal
    
    pvals = np.zeros((len(ks),1))
    for ind in range(len(ks)):
        k            = ks[ind]
        m            = abs_moment(x, k)
        mean         = mn(k, sd_emp, N)
        sd           = stdev(k, sd_emp, N)
        z            = (m - mean)/sd
        pvals[ind]   = 1 - st.norm.cdf(abs(z))

    (H, pvals_corr)  = mne.stats.fdr_correction(pvals, alpha=pthr, method='indep')
    
    if len(H[np.where(H == True)]) > 0:
        H0 = True
    else:
        H0 = False
    ks               = np.reshape(np.asarray(ks), (len(ks),1)) 
    Psubthr          = pvals_corr[pvals_corr < pthr] 
    Ksubthr          = ks[pvals_corr < pthr]
    
    return [H, pvals_corr, H0, Psubthr, Ksubthr]