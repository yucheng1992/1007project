# author: Wenjia Wu(ww933):90% and Yucheng Lu(yl2695):10%

import pandas as pd
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

from StateStarDistributionExceptions import *

try:
    data = pd.read_csv('yelp_restaurant_only_dataset.csv')
except IOError:
    print 'Sorry, cannot read file, please check the file again.'



def StateSearch(df, state_name):
    """
    StateSearch searches for restaurant information in a state, it is used in PlotPieChartForOneState function in this
    module

    :param df: a DataFrame
    :param state_name: a state abbreviation from {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    :return:each restaurant's star in the specific state
    """

    # state_info is a DataFrame which stores all the information about the restaurants in a certain state
    state_info = df[df['state'].str.contains(state_name, case=False)]

    # if search_result is empty, which means that there is no match for partial_name, an exception raises
    if state_info.empty:
        raise StateSearchNoResultError('Sorry, no result. Note: the available options for the states can'
                                       'only be: ON, ELN, EDH, MLN, WI, NY, KHL, AZ, CA, NV')
    else:
        return state_info['stars']


def SaveToDict(df):
    """
    This function is used after StateSearch(df, state_name)
    I.e. df = StateSearch(df, state_name)
    For example:
    if df = StateSearch(data, 'WI')
    Using SaveToDict(df) will get {4.5: 117, 3.5: 170, 2.0: 14, 3.0: 111, 4.0: 161, 5.0: 55, 2.5: 66, 1.0: 8, 1.5: 19}
    Note: it is used in PlotPieChartForOneState function in this module

    :param df: a DataFrame
    :return: the possible star values and the number of restaurants with the corresponding star value
    """

    star_count = {}

    for star in set(df.values):
        star_count[star] = len(df[df.values == star])
    return star_count


def PlotStarDistribution():
    """
    PlotStarDistribution generates six plots
    Here we ignored other possible state options, such as ELN or CA, because, in our DataSet, there are not enough
    restaurants in the certain states to let us evaluate the distribution

    :return: 6 histograms to show the distributions of stars in six states: ON, EDH, MLN, WI, AZ, NV
    """

    fig, axs = plt.subplots(3, 2)
    fig.subplots_adjust(hspace=.5, wspace=.5)
    axes = axs.ravel()

    i = 0

    for state in ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']:

        df = StateSearch(data, state)

        df.hist(bins=200, ax=axes[i], color='k', alpha=.5)
        axes[i].set_title(state)

        i += 1

    plt.suptitle('Distribution of stars in each state')
    plt.show()


def PlotPieChartForOneState(state):
    """
    PlotPieChartForOneState function plots a pie chart for a certain state
    Note: Though this function can plot a pie chart for any state in
                                          {'ON', 'ELN', 'EDH', 'MLN', 'WI', 'NY', 'KHL', 'AZ', 'CA', 'NV'}
    only six states - ON, EDH, MLN, WI, AZ, NV - get meaningful pie charts

    :param state: any element from {'ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV'}
    :return: a pie chart
    """

    if state in ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']:
        pass
    else:
        raise NoValidPieChartForOneStateError('Sorry, only states from [\'ON\', \'EDH\', \'MLN\', \'WI\', \'AZ\', '
                                              '\'NV\'] can generate meaningful pie chart')

    # df is a Series with star information in 'state'
    df = StateSearch(data, state)

    # star_count is a dictionary with keys set to be the restaurants' star values and values set to be the number of
    # restaurants with a certain star value
    # e.g.: if state='AZ',
    #       star_count = {2.5: 623, 4.5: 1062, 2.0: 299, 3.0: 952, 4.0: 1544, 5.0: 929, 3.5: 1455, 1.0: 81, 1.5: 128}
    star_count = SaveToDict(df)

    # weights calculates the weights of each star value
    # pert stores the percentage of each star values
    weights = [float(x) / sum(star_count.values()) for x in star_count.values()]
    percent = [str(100 * (round(float(i), 2))) + '%' for i in weights]

    # pie_labels represents the star value with the percentage of the certain star values
    pie_labels = [str(x) + ' star: ' + y for x, y in zip(star_count.keys(), percent)]

    # cs generates some colors
    # It will be used in plotting the pie chart later
    cs = cm.Set1(np.arange(len(df.values)) / 10.)

    # Next, plot the pie chart
    patches, texts = plt.pie(star_count.values(), labels=star_count.keys(), labeldistance=1.05, colors=cs)
    plt.legend(patches, pie_labels, loc='upper right', bbox_to_anchor=(0.12, 1.), fontsize=9)

    plt.axis('equal')
    plt.title(state + ' : Restaurant Star Distribution')

    plt.show()


def PlotStateMeanStar():
    """
    In this function, we give a scatter plot showing mean stars in given states.
    """

    states = ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']

    state_mean = {}

    for state in states:
        mean = np.mean(data[data['state'] == state]['stars'])
        state_mean[state] = mean

    plt.scatter(np.arange(len(state_mean)), state_mean.values())
    plt.xticks(np.arange(len(state_mean)), state_mean.keys())
    plt.ylabel('mean stars')
    plt.title('Mean stars in states')

    plt.show()