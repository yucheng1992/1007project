# author: Wenying Liu(wl1207)
import unittest
from pandas import DataFrame, Series
from exceptionClass import num_topInputError, stateInputError
from searchRestaurantsByPopularity import searchRestaurantByPopularity


class testsearchRestaurantByPopularity(unittest.TestCase):
    '''
    Test the second part of the application.
    '''

    def setUp(self):
        '''
        set up testing data for the test.
        '''

        self.state1 = 'AZ'
        self.state2 = 'DS'
        self.num_top1 = 3
        self.num_top2 = -3


    def testsearchRestaurantByPopularity(self):
        '''
        test searchRestaurantByPopularity function
        '''

        # state:'AZ' and num_top = 3 should be a correct user input and thus it is expected to return a DataFrame.
        self.assertIsInstance(searchRestaurantByPopularity(self.state1,self.num_top1), DataFrame)

        # state:'DS' or num_top = -3 are not right user input, thus it is expected to raise an exception.
        self.assertRaises(num_topInputError, searchRestaurantByPopularity,self.state1, self.num_top2)
        self.assertRaises(stateInputError, searchRestaurantByPopularity,self.state2 ,self.num_top1)


if __name__ == '__main__':
    unittest.main()
