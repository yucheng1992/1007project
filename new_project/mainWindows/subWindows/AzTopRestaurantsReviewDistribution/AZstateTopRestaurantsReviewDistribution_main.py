# author: Wenying Liu(wl1207)

from AZstateTopRestaurantsReviewDistribution import AZstateRestaurantReviewDistribution
from exceptionClass import InputError
import sys


def main():

	while True:
	
		print "We have records in following states: AZ."
		print "Because of the limits of our canvas size, only num_top in [1,5] would work."
		
		# Get input from user for selected state and expected number of top popular restaurants.
        # Input doesn't follow the instruction will raise exception.
		
		try:
			num_top = int(raw_input('How many top popular restaurants in {} you want? \n'.format('AZ')))
			
			print 'This plots TOP {} popular restaurants in {}.'.format(num_top, 'AZ')
			AZstateRestaurantReviewDistribution(num_top)
			
		except(InputError, ValueError):
			print 'Invalid input, please follow the instruction. '
			
		except(KeyboardInterrupt,EOFError):
			print 'Thanks for using. '
			sys.exit()
			
if __name__ == '__main__':
	main()