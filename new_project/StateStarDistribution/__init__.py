__author__ = 'chianti'

'''
This module let the user search for a state in the U.S and then plot the star distribution for all the restaurants in
the state.

This Module contains four parts:

StateStarDistributionExceptions.py - exceptions

StateStarDistributionFuncs.py - functions:
                    StateSearch(df, state_name), SaveToDict(df), PlotStarDistribution(), PlotPieChartForOneState(state)

test_StateStarDistribution.py - unittest

StateValidity.py - classes and functions used to check the validity of a state name.
        It contains: StateName class, IsValidString function, IsValidState function
'''
