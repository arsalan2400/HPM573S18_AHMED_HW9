#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:18:30 2018

@author: Aslan
"""
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import scr.RandomVariantGenerators as rndClasses
import scr.EconEvalClasses as EconCls
import ParameterClassesAA as P
import InputDataAA as INPUT

###THE BELOW IS COPIED FROM THE MARKOVMODEL.PY in class###
class Patient:
    def __init__(self, id, parameters):
        """ initiates a patient
        :param id: ID of the patient
        :param parameters: parameter object
        """
        self._id = id
        # random number generator for this patient
        self._param = parameters
        # state monitor
        self._stateMonitor = PatientStateMonitor(parameters)
        # simulation time step
        self._delta_t = parameters.get_delta_t()

    def simulate(self, sim_length):
        """ simulate the patient over the specified simulation length """

        # random number generator for this patient
        self._rng = rndClasses.RNG(self._id)

        k = 0  # current time step

        # while the patient is alive and simulation length is not yet reached
        while self._stateMonitor.get_if_alive() and k*self._delta_t < sim_length:

            # find the transition probabilities of the future states
            trans_probs = self._param.get_transition_prob(self._stateMonitor.get_current_state())
            # create an empirical distribution
            empirical_dist = rndClasses.Empirical(trans_probs)
            # sample from the empirical distribution to get a new state
            # (returns an integer from {0, 1, 2, ...})
            new_state_index = empirical_dist.sample(self._rng)

            # update health state
            self._stateMonitor.update(k, P.HealthStats(new_state_index))

            # increment time step
            k += 1

    def get_survival_time(self):
        """ returns the patient's survival time"""
        return self._stateMonitor.get_survival_time()
###Modified from get_time_toAiDS(self):
    def get_these_stroke_times(self):
        """ returns the patient's time to stroke """
        return self._stateMonitor.get_these_stroke_times()

#STEP 2 is the PATIENTSTATEMONITOR. 
class PatientStateMonitor:
    """ to update patient outcomes (years survived, cost, etc.) throughout the simulation """
    def __init__(self, parameters):
        """
        :param parameters: patient parameters
        """
        self._currentState = parameters.get_initial_health_state() # current health state
        self._delta_t = parameters.get_delta_t()    # simulation time step
        self._survivalTime = 0          # survival time
        #Modified for stroke:
        self._timeToSTROKE = 0        # number of strokes
        self._ifDevelopedSTROKE = False   # if the patient developed Stroke

    def update(self, k, next_state):
        """
        :param k: current time step
        :param next_state: next state
        """

        # if the patient has died, do nothing
        if not self.get_if_alive():
            return

        # update survival time. .DEATH and .STROKE come from ParameterClassesAA
        if next_state == P.HealthStats.DEATH:
            self._survivalTime = (k+0.5)*self._delta_t  # corrected for the half-cycle effect

        # update time until Stroke
        if self._currentState != P.HealthStats.STROKE and next_state == P.HealthStats.STROKE:
            self._ifDevelopedSTROKE = True
            #the DELTA_T comes from InputDataAA.
            self._timeToSTROKE = self.DELTA_T+1   # add 1 if the patient develop stroke

        # update current health state
        self._currentState = next_state

###FROM THE CLASS FILE#####
    def get_if_alive(self):
        result = True
        if self._currentState == P.HealthStats.DEATH:
            result = False
        return result

    def get_current_state(self):
        return self._currentState

    def get_survival_time(self):
        """ returns the patient survival time """
        # return survival time only if the patient has died
        if not self.get_if_alive():
            return self._survivalTime
        else:
            return None

    def get_these_stroke_times(self):
        """ returns the number of strokes """
        # return only if the patient has developed stroke
        if self._ifDevelopedSTROKE:
            return self._timeToSTROKE
        else:
            return None

##I dont need the class PatientCostUtilityMonitor:##
##Skip to class Cohort####
            
class Cohort:
    def __init__(self, id, therapy):
        """ create a cohort of patients
        :param id: an integer to specify the seed of the random number generator
        """
        ##POP_SIZE comes from the input dataAA. 
        self._initial_pop_size = INPUT.POP_SIZE
        self._patients = []      # list of patients

        # populate the cohort
        for i in range(self._initial_pop_size):
            # create a new patient (use id * pop_size + i as patient id)
            if INPUT.PSA_ON:
                patient = Patient(id * self._initial_pop_size + i, P.ParametersProbabilistic(i, therapy))
            else:
                patient = Patient(id * self._initial_pop_size + i, P.ParametersFixed(therapy))
            # add the patient to the cohort
            self._patients.append(patient)
           

##Below is the same....####
    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :returns outputs from simulating this cohort
        """

        # simulate all patients
        for patient in self._patients:
            patient.simulate(INPUT.SIM_LENGTH)

        # return the cohort outputs
        return CohortOutputs(self)

    def get_initial_pop_size(self):
        return self._initial_pop_size

    def get_patients(self):
        return self._patients


class CohortOutputs:
    def __init__(self, simulated_cohort):
        """ extracts outputs from a simulated cohort
        :param simulated_cohort: a cohort after being simulated
        """

        self._survivalTimes = []        # patients' survival times
        self._timeToSTROKE = []        # patients' stroke times
#we dont need costs or utilities here.
        
        # survival curve
        self._survivalCurve = \
            PathCls.SamplePathBatchUpdate('Population size over time', id, simulated_cohort.get_initial_pop_size())

        # find patients' survival times
        for patient in simulated_cohort.get_patients():

            # get the patient survival time
            survival_time = patient.get_survival_time()
            if not (survival_time is None):
                self._survivalTimes.append(survival_time)           # store the survival time of this patient
                self._survivalCurve.record(survival_time, -1)       # update the survival curve

            # get the patient's time to AIDS
            time_To_STROKE = patient.get_these_stroke_times()
            if not (time_To_STROKE is None):
                self._time_To_STROKE.append(stroke_times)

        # summary statistics
        self._sumStat_survivalTime = StatCls.SummaryStat('Patient survival time is... ', self._survivalTimes)
        self._sumState_timeToSTROKE = StatCls.SummaryStat('Time until STROKE is...', self._timeToSTROKE)

    def get_survival_times(self):
        return self._survivalTimes

    def get_these_stroke_times(self):
        return self._timeToSTROKE

    def get_sumStat_survival_times(self):
        return self._sumStat_survivalTime

    def get_sumState_timeToSTROKE(self):
        return self._sumState_timeToSTROKE

    def get_survival_curve(self):
        return self._survivalCurve
