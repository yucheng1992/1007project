# author: Wenying Liu(wl1207)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
from exceptionClass import InputError



def AZstateRestaurantReviewDistribution(num_top):
    '''

    In this function, firstly, we select our all business in given state
    (Because most review records are in AZ, we will only look into one state this time.).

    Then, using the groupby-apply-combine method, we get a series of business_id
    according to its total number of received review in descending order.
    (We assume that review counts would rightly reflect its popularity among the area.);
    Since there are too many restaurants to plot in our canvas,
    we may restrict the number of top popular to be smaller than a given threshold(say 5).

    For each business id in the Series, we will trace back to the review dataset,
    find all historical reviews it has received,
    especially, we want to know how stars given by reviewers change over time.
    (As this might reflect the change of the quality in reality.)
    '''
	
    state = 'AZ'
    #Load yelp_training_set_review dataset.
    #Transform the date columns into readable format.
    #Select only first four columns which are relevant to our analysis.
    
    try:
        review = pd.read_csv('yelp_training_set_review.csv')
    except IOError:
        print "Sorry, could not read file. Please check again."
		
    review['date'] = pd.to_datetime(review['date'])
    review = review.ix[:, :5]

    #Load yelp_training_set_business file.
    #Select only 'business_id','name','state' columns which are relevant to our analysis.

    try:
        business = pd.read_csv('yelp_training_set_business.csv')
    except IOError:
        print "Sorry, could not read file. Please check again."

    business = business[['business_id','name','state']]

    #Merge review dataset with business dataset.

    review = review.merge(business, on = 'business_id',how = 'left')

    # Drop the records where business_id is invalid.
    mask = [review['business_id'] != '#NAME?', review['business_id'] != '#VALUE!']
    review = review[mask[0] & mask[1]]
	
	
    # Check if we get an input num_top following the instruction.
    try:
        num = int(num_top)
        if num not in [1, 2, 3, 4, 5]:
            raise InputError('Wrong num_top. ')
    except:
        raise InputError('Wrong num_top. ')
	
	
    reviewInState = review[review['state']==state]
	
    # Groupby the reviewInState['stars'] according to each business_id.
    # Get the sorted index of business_id,
    # according to the total number of reviews each business_id has received in descending order.
	
    groupby_review = reviewInState['stars'].groupby(by=reviewInState.business_id)
    review_count = groupby_review.size()
    review_count.sort(ascending=False)
    ids = review_count.index[:num]

    # Get the plot.
	
    fig = plt.figure()

    for i in range(len(ids)):
	
        # If input(num_top) > length of records we have, we could only plot all records we have.
        ax = fig.add_subplot(min(num,len(review_count)),1,i)

        # Sort all the reviews for certain business_id in date order. So that the time series plot would reflect
        # how stars given by reviewers change over time.
        id_review = reviewInState[reviewInState['business_id']==ids[i]].sort(columns='date')

        dates = matdates.date2num(id_review['date'])
		
        plt.plot_date(dates,id_review['stars'],alpha=0.3, color='red')
        plt.yticks(np.arange(7))
        Y_label = review[review['business_id'] == ids[i]].iloc[0]['name']

        plt.title(Y_label+'review stars changes',fontsize=10)
        plt.tight_layout()
		
    plt.show()