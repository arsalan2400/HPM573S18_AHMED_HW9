#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:50:15 2018

@author: Aslan
"""

import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating mono therapy
# create a cohort
cohort_mono = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)
# simulate the cohort
simOutputs_mono = cohort_mono.simulate()

# simulating combination therapy
# create a cohort
cohort_combo = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.COMBO)
# simulate the cohort
simOutputs_combo = cohort_combo.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_mono, simOutputs_combo)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_mono, "Mono Therapy:")
SupportMarkov.print_outcomes(simOutputs_combo, "Combination Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_mono, simOutputs_combo)

# report the CEA results
SupportMarkov.report_CEA(simOutputs_mono, simOutputs_combo)