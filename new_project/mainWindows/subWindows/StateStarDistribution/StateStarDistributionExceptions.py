# author: Wenjia Wu(ww933)


class StateNotStringError(Exception):
    """
    StateNotStringError is used in class StateName, located under Package1and4.InputCheck
    If the input, which is supposed to indicate a state name, is not a string type, StateNotStringError raises.
    """

    pass


class StateNameContainNonAlphaError(Exception):
    """
    StateNameContainNonAlphaError is used in class StateName, located under Package1and4.InputCheck
    If the input, which is supposed to indicate a state name, contains non alphabetic characters(besides whitespace),
    StateNameContainNonAlphaError raises
    """

    pass


class InvalidStateNameError(Exception):
    """
    InvalidStateNameError is used in class StateName, located under Package1and4.InputCheck
    If the input, which is supposed to indicate a state name, is not an element from:
                                    {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    InvalidStateNameError raises
    """

    pass


class StateSearchNoResultError(Exception):
    """
    When the user is using the function StateSearch(df, state_name), while state_name is not a state abbreviation
    from {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}, StateSearchNoResultError raises
    """

    pass


class NoValidPieChartForOneStateError(Exception):
    """
    NoValidPieChartForOneStateError is used in PlotPieChartForOneState located under StateStarDistributionFuncs.py
    If the state from PlotPieChartForOneState(state) is not an element from ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV'],
    raise NoValidPieChartForOneStateError

    """

    pass
