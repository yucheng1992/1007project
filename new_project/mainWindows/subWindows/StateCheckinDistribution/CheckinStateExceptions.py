# author: Wenjia Wu(ww933)


class InvaldStateForCheckinError(Exception):
    """
    This error raises when a state doesn't belong to ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']
    This exception is used in checkin_state_check(state) function, located under CheckinStateCheck.py
    """
    pass