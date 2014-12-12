# author: Wenying Liu(wl1207)

import unittest
from pandas import DataFrame, Index
from popularRestaurantsInState.exceptionClass import InputError
from popularRestaurantsInState.popRestaurantInState import popRestaurantInState


class testpopRestaurantInState(unittest.TestCase):
    '''
    This is the test for the function popRestaurantInState.
    '''
    def setUp(self):
        '''
        set up test data for the test.
        '''
        self.state = 'AZ'
        self.num_top = 10

    def testpopRestaurantInState(self):
        '''
        Test the given function.
        '''
        self.assertRaises(InputError, popRestaurantInState, self.state, self.num_top)


if __name__ == '__main__':
    unittest.main()