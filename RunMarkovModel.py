#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:43:46 2018

@author: Aslan
"""

import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import SamplePathClasses as PathCls
import FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with HIV',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)
# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Mono therapy:')
