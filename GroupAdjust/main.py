# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:47:21 2015

@author: djunh
"""


from __future__ import print_function

import datetime

import numpy as np
import pandas as pd
import statsmodels.api as sm



class GroupAdjust():
    """
    Carries out a basic Moving Average Crossover strategy with a
    short/long simple weighted moving average. Default short/long
    windows are 100/400 periods respectively.
    """

    def __init__(self):
        """
        Initialises the Moving Average Cross Strategy.

        Parameters:
        bars - The DataHandler object that provides bar information
        events - The Event Queue object.
        short_window - The short moving average lookback.
        long_window - The long moving average lookback.
        """
       
    
 

       


if __name__ == "__main__":
    vals       = [  1  ,   2  ,   3  ]
    ctry_grp   = ['USA', 'USA', 'USA']
    state_grp  = ['MA' , 'MA' ,  'CT' ]
    
    x = np.array([2,3,1,0])
    