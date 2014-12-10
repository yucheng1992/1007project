__author__ = 'chianti'

from StateValidity import *
from StateStarDistributionFuncs import *
import unittest


class StateNameTests(unittest.TestCase):
    """
    This class is used to test the class StateName, located under StateValidity.py in StateStarDistribution module
    I.e: this class tests whether StateName can correctly check the validity of the input, which is supposed to indicate
    a state, and raise the corresponding exceptions if necessary.
    """

    def test_non_string_state(self):

        self.assertRaises(StateNotStringError, StateName, 222)

    def test_non_alpha_state(self):

        self.assertRaises(StateNameContainNonAlphaError, StateName, 'wi*')

    def test_invalid_state(self):

        self.assertRaises(InvalidStateNameError, StateName, 'WW')

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