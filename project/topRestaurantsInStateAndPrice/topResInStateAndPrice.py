import pandas as pd
import matplotlib.pyplot as plt
from exceptionClass import InputError

f = pd.read_csv('yelp_restaurant_only_dataset.csv')

def restaurantInStateandPrice(state, price, num_top):
	'''
	According to Yelp's definition, there are four categories in price ranges.
	$ -- corresponding to '1' in our data, price range: under 10;
	$$ -- corresponding to '2' in our data, price range:  $11-30;
	$$$ -- corresponding to '3' in our data, price range: $31-60;
	$$$$ -- corresponding to '4' in our data, price range: Above $61.
	'''

	if state not in ['WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL'] :
		raise InputError('Wrong state. ')
		
	if price not in [1,2,3,4]:
		raise InputError('Wrong price range. ')
		
	if not(num_top > 0):
		raise InputError('Wrong number of TOP. ')
	
	
	select_restaurants = f[(f['state'] == state) & (f['attributes_Price Range'] <= price)]
	sorted_restaurants = select_restaurants.sort(['stars','review_count','name'],ascending=False)
	
	return sorted_restaurants[:num_top][['name', 'city', 'attributes_Price Range', 'state', 'stars']]

def restaurantRegionPlot(restaurants):
	
	# The parameter 'restaurants' should be a DataFrame passed from above restaurantInStateandPrice function.
	# And the function will return a pie graph showing the regions where these top restaurants are in.
    plt.figure()

    topRestaurants = restaurants.set_index('name')
    topRestaurants['city'].value_counts().plot(kind = 'pie', figsize=(6,6))
	
    plt.show()