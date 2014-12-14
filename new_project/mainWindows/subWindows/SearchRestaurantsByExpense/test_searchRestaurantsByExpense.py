# author: Wenying Liu(wl1207)
import unittest
from pandas import DataFrame, Series
from exceptionClass import num_topInputError, stateInputError, priceInputError
from searchRestaurantsByExpense import searchRestaurantByExpenses


class testsearchRestaurantByPopularity(unittest.TestCase):
   
    '''
    Test the function searchRestaurantByExpenses.
    '''

    def setUp(self):
        
		'''
        set up testing data for the test.
		'''

		self.state1 = 'AZ'
		self.state2 = 'DS'
		self.price1 = 3
		self.price2 = 10
		self.num_top1 = 3
		self.num_top2 = -3


    def testsearchRestaurantByExpenses(self):
        
		'''
		test searchRestaurantByExpenses function
        '''
		
		# state:'AZ', price = 3 and num_top = 3 should be a correct user input and thus it is expected to return a DataFrame.
		self.assertIsInstance(searchRestaurantByExpenses(self.state1,self.price1, self.num_top1), DataFrame)

		# state:'DS', price = 10 or num_top = -3 are not right user input, thus it is expected to raise an exception.
		self.assertRaises(num_topInputError, searchRestaurantByExpenses,self.state1, self.price1, self.num_top2)
		self.assertRaises(stateInputError, searchRestaurantByExpenses,self.state2 ,self.price1, self.num_top1)
		self.assertRaises(priceInputError, searchRestaurantByExpenses,self.state1 ,self.price2, self.num_top1)

if __name__ == '__main__':
    unittest.main()
