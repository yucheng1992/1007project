from popRestaurantInState import popRestaurantInState
from exceptionClass import InputError
import sys

def main():

	while True:
	
		print "We have records in following states: WI, AZ, NV, CA, ON, EDH, ELN, MLN, NY, KHL."
		print "Because of the limits of our canvas size, only num_top in [1,5] would work."
		
		# Get input from user for selected state and expected number of top popular restaurants.
        # Input doesn't follow the instruction will raise exception.
		
		try:
		
			state = raw_input('Which state do you want to look into? \n')
			num_top = int(raw_input('How many top popular restaurants in {} you want? \n'.format(state)))
			
			print 'This plots TOP {} popular restaurants in {}.'.format(num_top, state)
			popRestaurantInState(state,num_top)
			
		except(InputError, ValueError):
			print 'Invalid input, please follow the instruction. '
		except(KeyboardInterrupt,EOFError):
			print 'Thanks for using. '
			sys.exit()
			
if __name__ == '__main__':
	main()