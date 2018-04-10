#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 12:22:06 2018

@author: Aslan
"""
###....HW9-7....######

import ParameterClassesAA as P
import MarkovModelClassesAA as MarkovCls
import SamplePathClasses as PathCls
import FigureSupport as Figs
import InputDataAA as Data
import FormatFunctions as F

#get mean number of strokes without the drug
cohort = MarkovCls.Cohort(id= 0, therapy = P.Therapies.withoutdrug)
simOutput = cohort.simulate()
strokecount_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumState_timeToSTROKE().get_mean(),
        interval=simOutput.get_sumState_timeToSTROKE().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("  Estimate of mean times of stroke and {:.{prec}%} confidence interval without drug is... :".format(1 - Data.ALPHA, prec=0),
      strokecount_mean_CI_text)

# graph histogram for this non-drug group
Figs.graph_histogram(
    data=simOutput.get_these_stroke_times(),
    title='Stroke Count if the Patient Does Not Receive the Heart-Drug Intervention',
    x_label='Survival time (years)',
    y_label='Stroke Counts (#)',
    bin_width=1
    )


####NOW for the ppl with the drug ######
    

#get mean number of strokes with the drug
Adjusted_Cohort = MarkovCls.Cohort(id=0, therapy=P.Therapies.newdrug)
new_simOutputs = Adjusted_Cohort.simulate()
new_strokecount_mean_CI_text = F.format_estimate_interval(
        estimate=new_simOutputs.get_sumState_timeToSTROKE().get_mean(),
        interval=new_simOutputs.get_sumState_timeToSTROKE().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("  Estimate of mean times of stroke and {:.{prec}%} confidence interval with Heart drug is...:".format(1 - Data.ALPHA, prec=0),
      new_strokecount_mean_CI_text)

# graph histogram for this yes drug group
Figs.graph_histogram(
    data=new_simOutputs.get_these_stroke_times(),
    title='Stroke Count if the Patient Takes the Heart-Drug Intervention',
    x_label='Survival time (years)',
    y_label='Stroke Counts (#)',
    bin_width=1
    )
