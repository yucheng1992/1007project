__author__ = 'chianti'
import unittest

from StateCheckinDistribution.CheckinStateCheck import *


class ValidCheckinStateTest(unittest.TestCase):
    """
    This test is used to test the checkinstatecheck function located under CheckinStateCheck.py
    """

    def non_alpha_state(self):
        self.assertRaises(ValueError, checkin_state_check, '33')

    def invalid_checkin_state(self):
        self.assertRaises(InvaldStateForCheckinError, checkin_state_check, 'NY')

if __name__ == '__main__':

    unittest.main()