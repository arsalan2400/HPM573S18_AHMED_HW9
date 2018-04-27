#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:43:46 2018
@author: Aslan
"""

import ParameterClassesAA as P
import MarkovModelClassesAA as MarkovCls
import SupportMarkovModelAA as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.newdrug)

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
SupportMarkov.print_outcomes(simOutputs, 'new therapy:')
