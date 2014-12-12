# author: Wenjia Wu(ww933)

from StateStarDistributionExceptions import *


class StateName():
    """
    StateName class is used to test whether the input, which is supposed to indicate a state, is a valid one.
    I.e: this class helps to check whether the input is an element from:
                {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    """

    def __init__(self, input_state):

        self.state_name = input_state

        # First, check whether self.name is a string type
        if IsValidString(self.state_name):
            pass
        else:
            raise StateNotStringError('Not String! The input is supposed to be a string type!')

        # Remove spaces from self.name and make it all upper letters
        self.no_space_state_name = self.state_name.replace(' ', '')
        self.upper_state_name = self.no_space_state_name.upper()

        # Check whether the input contains non alphabetic characters, after removing the white spaces in it
        if str.isalpha(self.upper_state_name):
            pass
        else:
            raise StateNameContainNonAlphaError('There exist non alphabetic characters that I can not recognize!')

        # Check whether the input is an element from:
        #                       {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
        if IsValidState(self.upper_state_name):
            pass
        else:
            raise InvalidStateNameError('Sorry, cannot recognize the state name! ')

    def __repr__(self):
        return 'StateName(%s)' % self.upper_state_name.strip()  # Note: removed leading and ending spaces here

    def __str__(self):
        return self.upper_state_name.strip().upper()   # Note: removed leading and ending spaces here


def IsValidString(content):
    """
    IsValidString(content) checks whether content is a string type
    It is used in StateName class, located under StateValidity.py in StateStarDistribution module

    :param content: the input given by the user
    :return:True if the type of content is string
            False if the type of content is not string
    """

    if type(content) == str:
        return True
    else:
        return False


def IsValidState(content):
    """
    IsValidState(content) checks whether content is an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    It is used StateName class, located under Package1and4/InputCheckClasses.py

    :param content: the input given by the user, which is supposed to indicate a state name
    :return:True if content is an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
            False if content is not an element from:
                                 {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    """

    valid_state = ['ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV']
    if content in valid_state:
        return True
    else:
        return False