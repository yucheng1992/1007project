# author: Wenjia Wu(ww933)
import unittest

from CheckinStateCheck import *


class ValidCheckinStateTest(unittest.TestCase):
    """
    This test is used to test the checkin_state_check function located under CheckinStateCheck.py
    """

    def test_non_alpha_state1(self):
        """
        test whether checkin_state_check(state) will raise ValueError then the parameter state is not a case-based one
        """
        self.assertRaises(ValueError, checkin_state_check, 33)

    def test_non_alpha_state2(self):
        """
        test whether checkin_state_check(state) will raise InvaldStateForCheckinError then the parameter state is a
        non-alphabetic one
        """
        self.assertRaises(InvaldStateForCheckinError, checkin_state_check, '*')

    def test_invalid_checkin_state(self):
        """
        test whether checkin_state_check(state) will raise InvaldStateForCheckinError then the parameter state is an
        invalid one. Note: there are only six valid choices for the parameter state
        I.e: the parameter state is not an element from ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']
        """
        self.assertRaises(InvaldStateForCheckinError, checkin_state_check, 'NY')

if __name__ == '__main__':

    unittest.main()
