# author: Wenjia Wu(ww933)

from CheckinStateExceptions import *


def checkin_state_check(state):
    """
    This function is used to check whether a state is a valid one in the check-in record.
    I.e: whether the state is an element from ['ON', 'EDH', 'MLN', 'WI', 'KHL', 'AZ', 'NV']
    :param state: an abbreviation for a state
    :return: an error if the state is invalid in this case, otherwise pass
    """
    # First, check whether the parameter state is case-based. If not, raise ValueError
    try:
        state = state.upper()
    except:
        raise ValueError

    # Second, check whether the parameter state is a valid one. Note: there are only six valid choices for the parameter
    if state in ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']:
        pass
    else:
        raise InvaldStateForCheckinError('Sorry, invalid state for check-in records.')

