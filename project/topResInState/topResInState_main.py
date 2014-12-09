from topResInState import topRestaurantsInState, restaurantStarsPlot, restaurantsMoreInformation
from exceptionClass import InputError
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
			restaurants = topRestaurantsInState(state, num_top)
			print restaurants['name']
			
			print "Show stars these restaurants have. "
			restaurantStarsPlot(restaurants)
			
			print "Show more detailed information. "
			print restaurantsMoreInformation(restaurants)
			
		except (InputError, ValueError):
			print 'Invalid input, please follow the instruction. '
			
		except (KeyboardInterrupt, IOError):
			print 'Thanks for using. '
			sys.exit()
		
	
if __name__ == '__main__':
	main()