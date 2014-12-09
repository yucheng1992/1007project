import unittest
from pandas import DataFrame, Index
from exceptionClass import InputError
from popRestaurantInState import popRestaurantInState


class testpopRestaurantInState(unittest.TestCase):

	def setUp(self):

		self.state1 = 'AZ'
		self.state2 = 'abc'
		self.num_top1 = 5
		self.num_top2 = 10

	def testpopRestaurantInState(self):
		#self.assertIsInstance(popRestaurantInState(self.state1,self.num_top1),Index)
		self.assertRaises(InputError, popRestaurantInState, self.state2,self.num_top1)
		self.assertRaises(InputError,popRestaurantInState,self.state1,self.num_top2)

if __name__ == '__main__':
    unittest.main()
