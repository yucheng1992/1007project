# author: Wenying Liu(wl1207)
import unittest
from pandas import DataFrame, Index
from exceptionClass import InputError
from AZstateTopRestaurantsReviewDistribution import AZstateRestaurantReviewDistribution


class testAZstateRestaurantReviewDistribution(unittest.TestCase):
    '''
    This is the test for the function AZstateRestaurantReviewDistribution.
    '''
    def setUp(self):
        '''
        set up test data for the test.
        '''
        self.state = 'AZ'
        self.num_top = 10

    def testAZstateRestaurantReviewDistribution(self):
        '''
        Test the given function.
        '''
        self.assertRaises(InputError, AZstateRestaurantReviewDistribution, self.num_top)


if __name__ == '__main__':
    unittest.main()
