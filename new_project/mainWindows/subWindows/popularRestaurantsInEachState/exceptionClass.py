# author: Wenying Liu(wl1207)

class InputError(Exception):
    """
    This exception will raise when user input does not follow the instruction.
    Either because the input value is out of value range or not contained in the records,
    or it is in a wrong type.
    """
    pass