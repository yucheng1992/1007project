# author: Wenying Liu(wl1207)

from searchRestaurantsByPopularity import searchRestaurantByPopularity, restaurantStarsPlot, restaurantsMoreInformation
from exceptionClass import stateInputError,num_topInputError
import pandas as pd
import sys


def main():
	
	while True:
	
		print "We have records in following states: WI, AZ, NV, CA, ON, EDH, ELN, MLN, NY, KHL."
		
		# Get input from user for selected state and number of top restaurants would display. 
		# Input doesn't follow the instruction will raise exception.
		
		try:
			state = raw_input('Which state do you want to look into? \n')
			num_top = int(raw_input('How many TOP restaurants do you want to see? \n'))
		
			print "These are TOP 10 restaurants in {}. ".format(state)
			restaurants = searchRestaurantByPopularity(state, num_top)
			print restaurants['name']
			
			print "Show stars these restaurants have. "
			restaurantStarsPlot(restaurants)
			
			print "Show more detailed information. "
			print restaurantsMoreInformation(restaurants)
			
		except(num_topInputError, ValueError):
			print 'Invalid input for num_top, please follow the instruction.' 
			
		except (stateInputError):
			print 'Invalid input for state, please follow the instruction. '
		
			
		except (KeyboardInterrupt, IOError):
			print 'Thanks for using. '
			sys.exit()
		
	
if __name__ == '__main__':
	main()