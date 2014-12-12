# author: Wenjia Wu(ww933)

from CheckinDistributionFuncs import *
import sys


def main():

    # Read the data
    business_data = read_business_data()
    checkin_data = read_checkin_data()

    # Merge two data sets
    total_data = merge_two_df(business_data, checkin_data)

    while True:
        state = raw_input('Type in a state from [ON, EDH, MLN, WI, KHL, AZ, NV]:  ')

        # Use checkin_state_check to check the validity of the input
        try:
            checkin_state_check(state)
            break

        # if receiving KeyboardInterrupt or SystemExit, double check
        except KeyboardInterrupt or SystemExit:
            double_check = raw_input('Do you want to quit? (Y/N)')
            if double_check == 'YES' or double_check == 'Y' or double_check == 'yes' or double_check == 'y':
                sys.exit()
            else:
                print 'Continuing... '

        # if receiving InvaldStateForCheckinError, print a message and then go back to the beginning of the loop
        except InvaldStateForCheckinError:
            print 'Invalid, please try again.'

    # Make the valid input upper-cases, and then plot the corresponding check-in distribution
    state = state.upper()
    plot_checkin_distribution(total_data, state)

if __name__ == '__main__':
    main()


