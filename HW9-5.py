#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 12:42:06 2018

@author: Aslan
"""
###HW9-5######

import ParameterClassesAA as P
import MarkovModelClassesAA as MarkovCls
import SamplePathClasses as PathCls
import FigureSupport as Figs
import InputDataAA as Data
import FormatFunctions as F

##this is a copy from the supportmarkov.py and is essentially what's in Q3, but we run it with the new drug instead of no drug ####
Adjusted_Cohort = MarkovCls.Cohort(id=0, therapy=P.Therapies.newdrug)
new_simOutputs = Adjusted_Cohort.simulate()
survival_mean_CI_text_new = F.format_estimate_interval(
        estimate=new_simOutputs.get_sumStat_survival_times().get_mean(),
        interval=new_simOutputs.get_sumStat_survival_times().get_t_CI(alpha=Data.ALPHA),
        deci=2)

print("  The new estimate of mean survival time and {:.{prec}%} confidence interval with the new drug is... :".format(1 - Data.ALPHA, prec=0),
      survival_mean_CI_text_new)
