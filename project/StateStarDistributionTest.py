__author__ = 'chianti'

from StateStarDistribution.StateValidity import *
from StateStarDistribution.StateStarDistributionFuncs import *
import unittest
from StateStarDistribution.StateStarDistributionExceptions import *


class StateNameTests(unittest.TestCase):
    """
    This class is used to test the class StateName, located under StateValidity.py in StateStarDistribution module
    I.e: this class tests whether StateName can correctly check the validity of the input, which is supposed to indicate
    a state, and raise the corresponding exceptions if necessary.
    """
    def setUp(self):
        '''
        set up test data
        '''
        self.stateName = None
        self.test1 = 222
        self.test2 = 'w*'
        self.test3 = 'WW'


    def tearDown(self):
        print 'Test stops!'

    def test_non_string_state(self):

        with self.assertRaises(StateNotStringError):
            self.stateName = StateName(self.test1)


    def test_non_alpha_state(self):

        with self.assertRaises(StateNameContainNonAlphaError):
            self.stateName = StateName(self.test2)

    def test_invalid_state(self):

        with self.assertRaises(InvalidStateNameError):
            self.stateName = StateName(self.test3)

    def test_valid_state(self):

        self.assertEqual(StateName('ny').__str__(), 'NY')


class PlotPieChartForOneStateTest(unittest.TestCase):
    """
    This class tests whether PlotPieChartForOneState(state) function can raise the corresponding exception when the
    parameter state is not from {'ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV'}
    """

    def test_invalid_state_pie_chart(self):

        self.assertRaises(NoValidPieChartForOneStateError, PlotPieChartForOneState, 'CA')

if __name__ == '__main__':

    unittest.main()