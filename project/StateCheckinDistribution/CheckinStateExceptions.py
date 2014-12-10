__author__ = 'chianti'


class InvaldStateForCheckinError(Exception):
    """
    This error raises when a state doesn't belong to ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']
    This exception is used in checkinstatecheck(state) function, located under CheckinStateCheck.py
    """
    pass