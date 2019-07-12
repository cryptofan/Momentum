#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:33:19 2019

@author: nataliabielczyk
"""


def effect_size(p):
    '''Converting a p-value to an effect size:
    '''
    snr = - math.log10(p)
    return snr