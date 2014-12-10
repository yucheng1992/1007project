import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
from exceptionClass import InputError



def popRestaurantInState(state, num_top):
	
	'''
	
	In this function, firstly, we select our all business in given state.
	
	Then, using the groupby-apply-combine method, we get a series of business_id 
	according to its total number of received review in descending order.
	(We assume that review counts would rightly reflect its popularity among the area.);
	Since in some state there are too many restaurants to plot in our canvas, 
	we may restrict the number of top popular to be smaller than a given threshold.
	
	For each business id in the Series, we will trace back to the review dataset, 
	find all historical reviews it has received,
	especially, we want to know how stars given by reviewers change over time.
	(As this might reflect the change of the quality in reality.)
	
	There might be a little problem that, since in some state there are not enough reviews, 
	for example: user inputs num_top=10, wanting to see top 10 popular restaurants in a given state,
	but we only have 5 restaurants records in this state. In this case, we can only plot min(num_top,len(review))=5
	subplots, this change would show on the plot title.
	
	'''
	
	
	#Load yelp_training_set_review dataset.
	#Transform the date columns into readable format.
	#Select only first four columns which are relevant to our analysis. 

	review = pd.read_csv('yelp_training_set_review.csv')
	review['date'] = pd.to_datetime(review['date'])
	review = review.ix[:,:5]

	#Load yelp_training_set_business file.
	#Select only 'business_id','name','state' columns which are relevant to our analysis.
	

	business = pd.read_csv('yelp_training_set_business.csv')
	business = business[['business_id','name','state']]

	#Merge review dataset with business dataset. 

	review = review.merge(business, on = 'business_id',how = 'left')

	# Drop the records where business_id is invalid.
	mask = [review['business_id']!='#NAME?', review['business_id'] !='#VALUE!']
	review = review[mask[0]&mask[1]]
	
	# First check if we get an state input in records.	
	state = state.upper()
	if state not in ['WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL'] :
		raise InputError('Wrong state. ')
	
	# Check if we get an input num_top following the instruction.
	if num_top not in [1,2,3,4,5]:
		raise InputError('Wrong num_top. ')
	
	
	reviewInState = review[review['state']==state]
	
	# Groupby the reviewInState['stars'] according to each business_id.
	# Get the sorted index of business_id, 
	# according to the total number of reviews each business_id has received in descending order.
	
	groupby_review = reviewInState['stars'].groupby(by=reviewInState.business_id)
	review_count = groupby_review.size()
	review_count.sort(ascending=False)
	ids = review_count.index[:num_top]

	# Get the plot.
	
	fig = plt.figure()
	
	for i in range(len(ids)):
	
		# If input(num_top) > length of records we have, we could only plot all records we have.
		ax = fig.add_subplot(min(num_top,len(review_count)),1,i)
		
		# Sort all the reviews for certain business_id in date order. So that the time series plot would reflect
		# how stars given by reviewers change over time.
		id_review = reviewInState[reviewInState['business_id']==ids[i]].sort(columns='date')
		
		dates = matdates.date2num(id_review['date'])
        plt.plot_date(dates,id_review['stars'],alpha=0.3, color='red')
        plt.yticks(np.arange(7))
        Y_label = review[review['business_id'] == ids[i]].iloc[0]['name']
        plt.ylabel(Y_label,rotation='horizontal',fontsize='small',verticalalignment='top')
	
	plt.suptitle('Review stars changes for Top {} popular restaurant in {}.'.format(min(num_top,len(review_count)),state))
	plt.show()