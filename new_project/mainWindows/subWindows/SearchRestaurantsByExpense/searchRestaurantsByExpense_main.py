# author: Wenying Liu(wl1207)

from searchRestaurantsByExpense import searchRestaurantByExpenses, restaurantRegionPlot
from exceptionClass import stateInputError, priceInputError, num_topInputError
import pandas as pd
import sys


def main():
    
	'''
    main function of searchRestaurantByExpenses.
    '''

	while True:

		print "We have records in following states: WI, AZ, NV, CA, ON, EDH, ELN, MLN, NY, KHL."
		print "Price ranges from 1 to 4(inclusive). "

        # Get input from user for selected state and expected maximum cost.
        # Input doesn't follow the instruction will raise exception.
		try:
			state = raw_input('Which state do you want to look into? \n')
			price = int(raw_input('From 1 to 4, what is your maximum expected price?  \n'))
			num_top = int(raw_input('How many restaurants meeting the requirements do you want to see? \n'))

			print "These are TOP 10 restaurants in {} with price below and containing {}. ".format(state, '$' * price)
			restaurants = searchRestaurantByExpenses(state, price, num_top)
			print restaurants[['stars', 'Price Range', 'city']]

			print "Show the regions where these top restaurants are in. "
			restaurantRegionPlot(restaurants)
			
		except (stateInputError):
			print 'Invalid input for state, please follow the instruction. '
		
		except (num_topInputError, ValueError):
			print 'Invalid input for num_top, please follow the instruction. '
		
		except (priceInputError):
			print 'Invalid input for price, please follow the instruction. '

		except (KeyboardInterrupt, IOError):
			print 'Thanks for using. '
			sys.exit()


if __name__ == '__main__':
    main()