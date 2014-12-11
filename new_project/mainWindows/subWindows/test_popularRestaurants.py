import unittest
from pandas import DataFrame, Index
from popularRestaurantsInState.exceptionClass import InputError
from popularRestaurantsInState.popRestaurantInState import popRestaurantInState


class testpopRestaurantInState(unittest.TestCase):
    def setUp(self):
        self.state1 = 'Wp'
        self.state2 = 'abc'
        self.num_top1 = 5
        self.num_top2 = 10

    def testpopRestaurantInState(self):
        self.assertRaises(InputError, popRestaurantInState, self.state2,self.num_top1)
        self.assertRaises(InputError, popRestaurantInState, self.state1, self.num_top2)


if __name__ == '__main__':
    unittest.main()
