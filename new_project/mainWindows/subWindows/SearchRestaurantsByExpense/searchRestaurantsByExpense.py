# author: Wenying Liu(wl1207):80% and Yucheng Lu(yl2695):20%

import pandas as pd
import matplotlib.pyplot as plt
from exceptionClass import stateInputError, priceInputError, num_topInputError


try:
	f = pd.read_csv('yelp_restaurant_only_dataset.csv')
except IOError:
	print "Sorry, could not read file. Please check again."
	

def searchRestaurantByExpenses(state, price, num_top):
    '''
    According to Yelp's definition, there are four categories in price ranges.
	$ -- corresponding to '1' in our data, price range: under 10;
	$$ -- corresponding to '2' in our data, price range:  $11-30;
	$$$ -- corresponding to '3' in our data, price range: $31-60;
	$$$$ -- corresponding to '4' in our data, price range: Above $61.
    '''
    state = state.upper()
    if state not in ['WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL'] :
        raise stateInputError('Wrong state. ')

    try:
        target_price = int(price)
        if target_price not in [1,2,3,4]:
            raise priceInputError('Wrong price range. ')
    except:
        raise priceInputError('Wrong price range. ')

    try:
        num = int(num_top)
        if num < 0:
            raise num_topInputError('Wrong number of TOP. ')
    except:
        raise num_topInputError('Wrong number of TOP. ')
	
	
    select_restaurants = f[(f['state'] == state) & (f['attributes_Price Range'] <= target_price)]
    sorted_restaurants = select_restaurants.sort(['stars','review_count','name'], ascending=False)
    sorted_restaurants['Price Range'] = sorted_restaurants['attributes_Price Range']

    sorted_restaurants.dropna()
    sorted_restaurants = sorted_restaurants.set_index(['name'])
    return sorted_restaurants[:num if num < 6 else 5][['city', 'Price Range', 'state', 'stars']]


def restaurantRegionPlot(restaurants):
    '''
	The parameter 'restaurants' should be a DataFrame passed from above searchRestaurantByExpenses function.
    And the function will return a pie graph showing the regions where these top restaurants are in.
	'''

    plt.figure()


    plt.pie(restaurants['city'].value_counts(), labels=restaurants['city'].unique(), autopct='%.2f')
    plt.title('The regions of the top restaurants')
    plt.show()