__author__ = 'chianti'

import pandas as pd
import matplotlib.pyplot as plt

from StateCheckinDistribution.CheckinStateCheck import *


def read_business_data():
    """
    Read yelp_restaurant_only_dataset.csv into a DataFrame, and drop the columns except 'business_id', 'name', 'state'
    :return: a DataFrame with only three columns: 'business_id', 'name' and 'state',containing restaurants' information
    """

    business_data = pd.read_csv('../yelp_restaurant_only_dataset.csv')
    business_data = business_data[['business_id', 'name', 'state']]

    return business_data


def read_checkin_data():
    """
    Read yelp_academic_dataset_checkin.csv into a DataFrame, fill the NaN values with 0, then drop the column 'type'
    :return: a cleaned DataFrame, containing check-in information
    """

    checkin_data = pd.read_csv('../yelp_academic_dataset_checkin.csv')
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
    try:
        checkin_state_check(state)
    except InvaldStateForCheckinError:
        print 'Invalid input for the state'

    check_Monday = whole_dataset[['checkin_info_{}-1'.format(str(x)) for x in range(24)]]
    check_Tuesday = whole_dataset[['checkin_info_{}-2'.format(str(x)) for x in range(24)]]
    check_Wednesday = whole_dataset[['checkin_info_{}-3'.format(str(x)) for x in range(24)]]
    check_Thursday = whole_dataset[['checkin_info_{}-4'.format(str(x)) for x in range(24)]]
    check_Friday = whole_dataset[['checkin_info_{}-5'.format(str(x)) for x in range(24)]]
    check_Saturday = whole_dataset[['checkin_info_{}-6'.format(str(x)) for x in range(24)]]
    check_Sunday = whole_dataset[['checkin_info_{}-0'.format(str(x)) for x in range(24)]]
    # Split the whole data set into seven parts, each one contains the information for each weekday

    Mon_dataset = check_Monday[check_Monday.index == state]
    Tue_dataset = check_Sunday[check_Tuesday.index == state]
    Wed_dataset = check_Sunday[check_Wednesday.index == state]
    Thu_dataset = check_Sunday[check_Thursday.index == state]
    Fri_dataset = check_Sunday[check_Friday.index == state]
    Sat_dataset = check_Sunday[check_Saturday.index == state]
    Sun_dataset = check_Sunday[check_Sunday.index == state]
    # For each of the seven data sets, only keep the rows corresponding to the state value and drop the others

    plt.plot(Mon_dataset.T)
    plt.plot(Tue_dataset.T)
    plt.plot(Wed_dataset.T)
    plt.plot(Thu_dataset.T)
    plt.plot(Fri_dataset.T)
    plt.plot(Sat_dataset.T)
    plt.plot(Sun_dataset.T)
    # Plot the check-in numbers for each day

    labels = ['0:00-1:00', '1:00-2:00', '2:00-3:00', '3:00-4:00', '4:00-5:00', '5:00-6:00', '6:00-7:00', '7:00-8:00',
              '8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00',
              '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00', '20:00-21:00', '21:00-22:00',
              '22:00-23:00', '23:00-24:00']
    x = range(0, 24)
    plt.xticks(x, labels, rotation=30, size=8)
    # Set the x-ticks

    plt.legend(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], loc='best')
    plt.xlabel('time')
    plt.ylabel('total number of check-ins')
    plt.title('Check-in Distribution in state %s' % state )

    plt.show()
