# author: Wenjia Wu(ww933):60% and Yucheng Lu(yl2695):40%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from CheckinStateCheck import *


def read_business_data():
    """
    Read yelp_restaurant_only_dataset.csv into a DataFrame, and drop the columns except 'business_id', 'name', 'state'
    :return: a DataFrame with only three columns: 'business_id', 'name' and 'state',containing restaurants' information
    """
    try:
        business_data = pd.read_csv('yelp_restaurant_only_dataset.csv')
    except IOError:
        print 'Sorry, cannot read file, please check the file again.'

    business_data = business_data[['business_id', 'name', 'state']]

    return business_data


def read_checkin_data():
    """
    Read yelp_academic_dataset_checkin.csv into a DataFrame, fill the NaN values with 0, then drop the column 'type'
    :return: a cleaned DataFrame, containing check-in information
    """
    try:
        checkin_data = pd.read_csv('yelp_academic_dataset_checkin.csv')
    except:
        print 'Sorry, cannot read file, please check the file again.'

    checkin_data = checkin_data.fillna(0)
    checkin_data = checkin_data.drop('type', 1)

    return checkin_data


def merge_two_df(business, check_in):
    """
    Merge two data sets, and return the merged data set, which is a DataFrame
    :param business:  a DataFrame containing the restaurants' information
    :param check_in:  a DataFrame containing the check-in information
    :return: a DataFrame with both the restaurants' information and the check-in information
    """

    merged = pd.merge(business, check_in, on='business_id')
    total_data = merged.groupby('state')
    total_data = total_data.sum()

    return total_data


def plot_checkin_distribution(whole_dataset, state):
    """
    This function generates a plot for the distribution of check-in records in the certain state.
    :param whole_dataset: the data set which contain both the restaurants' information and the check-in information
    :param state: any state from ['ON', 'EDH', 'MLN', 'WI', 'KHL', 'AZ', 'NV']
                  (for other states, there is simply no record or not enough record to plot meaningful plots)
    :return: a plot showing the distribution, from 0am to 24pm, for the check-in numbers in each state
    """
    state = state.upper()

    try:
        checkin_state_check(state)
    except InvaldStateForCheckinError:
        print 'Invalid input for the state'

    # Split the whole data set into seven parts, each one contains the information for each weekday
    check_Monday = whole_dataset[['checkin_info_{}-1'.format(str(x)) for x in np.arange(24)]]
    check_Tuesday = whole_dataset[['checkin_info_{}-2'.format(str(x)) for x in np.arange(24)]]
    check_Wednesday = whole_dataset[['checkin_info_{}-3'.format(str(x)) for x in np.arange(24)]]
    check_Thursday = whole_dataset[['checkin_info_{}-4'.format(str(x)) for x in np.arange(24)]]
    check_Friday = whole_dataset[['checkin_info_{}-5'.format(str(x)) for x in np.arange(24)]]
    check_Saturday = whole_dataset[['checkin_info_{}-6'.format(str(x)) for x in np.arange(24)]]
    check_Sunday = whole_dataset[['checkin_info_{}-0'.format(str(x)) for x in np.arange(24)]]

    # For each of the seven data sets, only keep the rows corresponding to the state value and drop the others
    Mon_dataset = check_Monday[check_Monday.index == state]
    Tue_dataset = check_Tuesday[check_Tuesday.index == state]
    Wed_dataset = check_Wednesday[check_Wednesday.index == state]
    Thu_dataset = check_Thursday[check_Thursday.index == state]
    Fri_dataset = check_Friday[check_Friday.index == state]
    Sat_dataset = check_Saturday[check_Saturday.index == state]
    Sun_dataset = check_Sunday[check_Sunday.index == state]

    # total_checkin_num contains 24 numbers, each of which indicates the total number, from Monday to Sunday, of
    # check-in during each hour period.
    total_checkin_num = Mon_dataset.values+Tue_dataset.values+Wed_dataset.values+Thu_dataset.values+Fri_dataset.values\
                         +Sat_dataset.values+Sun_dataset.values

    # checkin_hour_mean indicates the average number, from Monday to Sunday, of check-in during each hour period.
    checkin_hour_mean = total_checkin_num/7.0

    #  plot the check-in numbers for each day
    plt.plot(Mon_dataset.T)
    plt.plot(Tue_dataset.T)
    plt.plot(Wed_dataset.T)
    plt.plot(Thu_dataset.T)
    plt.plot(Fri_dataset.T)
    plt.plot(Sat_dataset.T)
    plt.plot(Sun_dataset.T)

    # plot the mean of checkin_hour_mean as a reference line
    plt.plot([0, 24], [checkin_hour_mean.mean(), checkin_hour_mean.mean()])

    # plot checkin_hour_mean
    plt.scatter(range(0, 24), checkin_hour_mean[0], color='black', s=8)

    # change the xticks from 0,1, ..., 23 to 0:00-1:00, 1:00-2:00, ..., 23:00-24:00
    labels = ['{}:00-{}:00'.format(str(x), str(x+1)) for x in range(24)]
    x = range(0, 24)
    plt.xticks(x, labels, rotation=30, size=8)

    plt.legend(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mean per day', 'Average per hour'], loc='best',
               fontsize=9)
    plt.xlabel('time')
    plt.ylabel('total number of check-ins')
    plt.title('Check-in Distribution in state %s' % state )

    plt.show()