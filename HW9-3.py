#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 11:30:06 2018

@author: Aslan
"""
###HW9-3######

import ParameterClassesAA as P
import MarkovModelClassesAA as MarkovCls
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import InputDataAA as Data
import scr.FormatFunctions as F


#We bring up the Cohort from MarkovModels... and which situation (drug/ no drug) from the Param classes. 
cohort = MarkovCls.Cohort(id= 0, therapy = P.Therapies.withoutdrug)
def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print(therapy_name)
    print("  Estimate of mean survival time and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
