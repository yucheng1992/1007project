# author: Wenjia Wu(ww933)

class NameSearchNoResultError(Exception):
    """
    When the user is using the function NameSearch(df, partial_name), while there is no partial_name in the 'name'
    feature in the df DataFrame, NameSearchNoResultError raises.
    """

    pass
