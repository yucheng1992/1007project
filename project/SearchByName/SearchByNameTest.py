__author__ = 'chianti'

from SearchByName.SearchByNameFuncs import *
import pandas as pd
import unittest



# Load the data set


class NameSearchNoResultErrorTest(unittest.TestCase):
    """
    This class is used to test whether NameSearch function, located under SearhByNameFuncs.py, can raise the correct
    exceptions for invalid input
    """
    def setUp(self):
        self.data = pd.read_csv('yelp_restaurant_only_dataset.csv')
        self.str1 = '$'
        self.str2 = '^'

    def test_name_search_special_character1(self):

        self.assertRaises(NameSearchNoResultError, NameSearch, self.data, self.str1)

    def test_name_search_special_character2(self):

        self.assertRaises(NameSearchNoResultError, NameSearch, self.data, self.str2)

if __name__ == '__main__':

    unittest.main()
