#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 09:42:06 2018

@author: Aslan
"""
###...HW9-6....#####

import ParameterClassesAA as P
import MarkovModelClassesAA as MarkovCls
import SamplePathClasses as PathCls
import FigureSupport as Figs
import InputDataAA as Data
import FormatFunctions as F


#First, run the graph without the drug. This is from SamplePathclasses.py#
##Note this is essentially copied from the SupportMarkovModel.py


 # graph survival curve
cohort = MarkovCls.Cohort(id= 0, therapy = P.Therapies.withoutdrug)
simOutput = cohort.simulate()
PathCls.graph_sample_paths(
    sample_paths=simOutput.get_survival_curve()
    title='Survival Curve without Drug Intervention',
    x_label='Simulation time step (year)',
    y_label='Number of alive patients',
    )

#Second, run the graph with the drug. This is from SamplePathclasses.py#
##Note this is essentially copied from the SupportMarkovModel.py


Adjusted_Cohort = MarkovCls.Cohort(id=0, therapy=P.Therapies.newdrug)
new_simOutputs = Adjusted_Cohort.simulate()
PathCls.graph_sample_paths(
    sample_paths=new_simOutputs.get_survival_curve(),
    title='Survival Curve with Heart Drug Intervention',
    x_label='Simulation time step (year)',
    y_label='Number of alive patients'
    )
