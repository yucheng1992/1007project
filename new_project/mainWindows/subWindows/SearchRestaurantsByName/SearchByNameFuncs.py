# author: Yucheng Lu(yl2695):50% and Wenjia Wu(ww933):50%

from SearchByNameExceptions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


def NameSearch(df, partial_name):
    """
    NameSearch function searches for a restaurant in the df given a partial_name
    :param df: a DataFrame
    :param partial_name: a string type
    :return: the selected rows of df with partial_name in the 'name' column, ignoring upper or lower case
    """

    # if the parameter partial_name is only '$' or '^', searching for the input will get all the restaurants'
    # information in our data set. So here we treat '$' and '^' as invalid input and raise an exception.
    # Note: some restaurants' names contain special characters such as ' # or numbers, so these are valid, indeed
    if partial_name == '$' or partial_name == '^':
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')

    # Search for certain information of the restaurants whose name match the input
    search_result = df[df['name'].str.contains(partial_name, case=False)]
    search_result = search_result[['name', 'city', 'state', 'stars', 'latitude', 'longitude']]

    # if search_result is empty, which means that there is no match for partial_name, an exception raises
    if search_result.empty:
        raise NameSearchNoResultError('Sorry, no result. Try another name ?')

    else:
        return search_result


def plot3dDistribution(df):
    """
    This function plots a 3d-distribution of stars according to the restaurants' latitude and longitude, corresponding
    to the user's input for a restaurant's name
    For example:
        If the user searches for restaurants whose names contain 'Chinese', he or she can roughly tell the distribution
        of the stars for those restaurants in the U.S

    :param df: a DataFrame, which is supposed to be part of the data set
    :return: a 3d-figure
    """
    latitudeRange = df['latitude']
    longitudeRange = df['longitude']
    starRange = df['stars']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(latitudeRange, longitudeRange, starRange)
    ax.set_xlabel('latitude')
    ax.set_ylabel('longitude')
    ax.set_zlabel('stars')
    ax.set_title("Restaurants' star distribution according to their location")
    plt.show()


def GetUsefulInfo(df):
    """
    GetUsefulInfo is used to get four features from df
    :param df: a DataFrame
    :return:the selected columns of the df
    """

    df = df.set_index(['name'])
    return df[['city', 'state', 'stars']]
