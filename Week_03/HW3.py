# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:07:36 2016

@author: cfd

Week 03 code
"""

import numpy as np
import random
import pandas as pd

##### Independent Random Variables Exercise #######

prob_W_I = np.array([[1/2, 0], [0, 1/6], [0, 1/3]])
prob_X_Y = np.array([[1/4, 1/4], [1/12, 1/12], [1/6, 1/6]])

# We can get marginal distributions Pw and Pi:
prob_W = prob_W_I.sum(axis = 1)
prob_I = prob_W_I.sum(axis = 0)

prob_X = prob_X_Y.sum(axis = 1)
prob_Y = prob_X_Y.sum(axis = 0)