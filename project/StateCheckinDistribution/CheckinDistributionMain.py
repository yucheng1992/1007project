__author__ = 'chianti'

from StateCheckinDistribution.CheckinDistributionFuncs import *


def main():

    business_data = read_business_data()
    checkin_data = read_checkin_data()
    # Read the data

    total_data = merge_two_df(business_data, checkin_data)
    # Merge two data sets

    while True:
        state = raw_input('Type in a state from [ON, EDH, MLN, WI, KHL, AZ, NV]:  ')
        try:
            checkin_state_check(state)
            break
        except InvaldStateForCheckinError:
            print 'Invalid, please try again'

    state = state.upper()
    plot_checkin_distribution(total_data, state)

if __name__ == '__main__':
    main()


