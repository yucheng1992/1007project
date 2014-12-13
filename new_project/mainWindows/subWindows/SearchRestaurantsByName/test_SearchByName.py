# author: Wenjia Wu(ww933)
from SearchByNameFuncs import *
import pandas as pd
import unittest


# Load the data set
data = pd.read_csv('yelp_restaurant_only_dataset.csv')


class NameSearchNoResultErrorTest(unittest.TestCase):
    """
    This class is used to test whether NameSearch function, located under SearhByNameFuncs.py, can raise the correct
    exceptions for invalid input
    """

    def test_name_search_special_character1(self):
        """
        test whether NameSearch(df, partial_name) will raise NameSearchNoResultError when partial_name is '$'
        """
        with self.assertRaises(NameSearchNoResultError):
            NameSearch(data, '$')

    def test_name_search_special_character2(self):
        """
        test whether NameSearch(df, partial_name) will raise NameSearchNoResultError when partial_name is '^'
        """
        with self.assertRaises(NameSearchNoResultError):
            NameSearch(data, '^')


if __name__ == '__main__':
    unittest.main()
