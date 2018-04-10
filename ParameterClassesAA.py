#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:01:36 2018

@author: Aslan
"""

from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputDataAA as Data
import MarkovModelClassesAA as MarkovCls
import RandomVariantGenerators as Random
import ProbDistParEstAA as Est

###First thing we need to do is set our healthstats and therapies. 
class HealthStats(Enum):
    WELL = 0
    STROKE= 1
    PS= 2
    DEATH = 3
class Therapies(Enum):
    withoutdrug = 0
    newdrug = 1

####note that the matrices are labelled based on the input data. Q3_TRANS_MATRIX
###is tied to therapy - without drug and ADJ_TRANS_MATRIX is tied to therapies.newdrug
    
class ParametersFixed():
    def __init__(self, drug):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T
        
        # Identify the initial health state, which is WELL. 
        self._initialHealthState = HealthStats.WELL
       
        # transition probability matrix of the selected therapy
        self._prob_matrix =Data.Q3_TRANS_MATRIX
        # update the transition probability matrix, the one with w the adjusted PS
        if self._drug == Therapies.newdrug:
            self._prob_matrix = Data.ADJ_TRANS_MATRIX

###This is just the relevant functions I pick out from ParameterClasses.py on the class list
    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]
