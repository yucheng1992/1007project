# author: Yucheng Lu(yl2695)

from Tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from subWindows.SearchRestaurantsByName.SearchByNameFuncs import *
from subWindows.StateStarDistribution.StateStarDistributionFuncs import *
import pandas as pd
from subWindows.SearchRestaurantsByPopularity.searchRestaurantsByPopularity import *
from subWindows.AzTopRestaurantsReviewDistribution.AZstateTopRestaurantsReviewDistribution import *
from subWindows.SearchRestaurantsByExpense.searchRestaurantsByExpense import *
from subWindows.StateCheckinDistribution.CheckinDistributionFuncs import *


class mainWindow():
    '''
    set up a class for this application and set up four sub-windows of the main window
    '''

    def __init__(self, top):
        '''
        initialize some necessary parameters of this application
        '''

        self.top = top

        # set the width and height for the main window
        self.WIDTH = 950
        self.HEIGHT = 534

        # set the background picture for the main window
        self.backImage = PhotoImage(file="yelp.gif")
        self.panel = Label(top, image=self.backImage)
        self.panel.pack(side='top', fill='both', expand='yes')

        # set up six main buttons of the main window which stand for six main functions.
        self.nameSearchButton = Button(text='Search Restaurants by Name', command=self.nameSearchWindow)
        self.nameSearchButton.place(relx=0.20, rely=0.33, anchor='center')

        self.expenseSearchButton = Button(text='Search Restaurants by Expense', command=self.expenseSearchWindow)
        self.expenseSearchButton.place(relx=0.20, rely=0.66, anchor='center')

        self.popularRestaurantsButton = Button(text='Search Restaurants by Popularity', command=self.popularRestaurantsWindow)
        self.popularRestaurantsButton.place(relx=0.52, rely=0.33, anchor='center')

        self.stateStarDistributionButton = Button(text="Star Distribution for each state", command=self.stateStarDistributionWindow)
        self.stateStarDistributionButton.place(relx=0.52, rely=0.66, anchor='center')

        self.checkinTimeDistributionButton = Button(text="Restaurants' Checkin Time Distribution", command=self.checkinTimeDistributionWindow)
        self.checkinTimeDistributionButton.place(relx=0.84, rely=0.66, anchor='center')

        self.AZreviewCountsDistributionButton = Button(text="AZ's popular restaurants' review changes", command=self.showAZReviewCountsDistributionWindow)
        self.AZreviewCountsDistributionButton.place(relx=0.84, rely=0.33, anchor='center')


    def nameSearchWindow(self):
        '''
        set up the first sub window -- name search window.
        '''

        # Initialize the window and set its size.
        self.nameSearchWindow = Toplevel()
        self.nameSearchWindow.geometry('{}x{}'.format(600, 600))

        # Initialize a stringvar to get the user's input at the entry
        self.ment = StringVar()

        # Initialize two labels to instruct the user to input.
        promptLabelOne = Label(self.nameSearchWindow, text='Input the name of the restaurant you hope to find:(For example: a)', fg='black')
        promptLabelTwo = Label(self.nameSearchWindow, text='If you want to search again, please press the clear button.')

        # Initialize the entry fot user inputs
        inputNameEntry = Entry(self.nameSearchWindow, textvariable=self.ment)

        promptLabelOne.place(relx=0.1, rely=0.25)
        promptLabelTwo.place(relx=0.1, rely=0.3)
        inputNameEntry.pack()
        inputNameEntry.place(relx=0.1, rely=0.35)

        # initialize the 3D plot button
        plot3dButton = Button(self.nameSearchWindow, text='3D plot', command=self.plot3D)
        plot3dButton.pack()
        plot3dButton.place(relx=0.7, rely=0.35)

        # initialize the search button
        searchButton = Button(self.nameSearchWindow, text='Search', command=self.showRestaurantSearchButton)
        searchButton.pack()
        searchButton.place(relx=0.42, rely=0.35)

        # initialize the clear button
        clearButton = Button(self.nameSearchWindow, text='Clear', command=self.new_canvas_search_window)
        clearButton.pack()
        clearButton.place(relx=0.56, rely=0.35)


    def popularRestaurantsWindow(self):
        '''
        set up the second sub window -- popular restaurants window.
        '''
        self.popularRestaurantsWindow = Toplevel()
        self.popularRestaurantsWindow.geometry('{}x{}'.format(600, 600))

        # initialize two stringvar to catch user's inputs
        self.stateMentPopularWindow = StringVar()
        self.numMentPopularWindow = StringVar()

        # set up some prompt labels
        stateLabel = Label(self.popularRestaurantsWindow, text='Please input the state whose popular restaurants you want to see: ')
        promptLabel = Label(self.popularRestaurantsWindow, text="(For Example:'WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL')")
        numLabel = Label(self.popularRestaurantsWindow, text="Please input the numbers of top restaurants you want to see:(For Example: 5)")

        # set up the necessary entries for user's inputs
        stateEntry = Entry(self.popularRestaurantsWindow, textvariable=self.stateMentPopularWindow)
        numEntry = Entry(self.popularRestaurantsWindow, textvariable=self.numMentPopularWindow)

        stateLabel.place(relx=0.10, rely=0.20)
        promptLabel.place(relx=0.1, rely=0.25)
        numLabel.place(relx=0.10, rely=0.35)
        stateEntry.pack()
        stateEntry.place(relx=0.10, rely=0.30)
        numEntry.pack()
        numEntry.place(relx=0.10, rely=0.40)

        # initialize the show button
        showButton = Button(self.popularRestaurantsWindow, text="Show", command=self.showTopRestaurantsPopularWindow)
        showButton.pack()
        showButton.place(relx=0.1, rely=0.47)

        # initialize the clear button
        clearButton = Button(self.popularRestaurantsWindow, text='Clear', command=self.new_canvas_popular_window)
        clearButton.pack()
        clearButton.place(relx=0.33, rely=0.47)

        # initialize the plot star and review counts button.
        plotStarAndReviewButton = Button(self.popularRestaurantsWindow, text='Plot star and review counts', command=self.plotTopRestaurantsPopularWinow)
        plotStarAndReviewButton.pack()
        plotStarAndReviewButton.place(relx=0.55, rely=0.47)


    def expenseSearchWindow(self):
        '''
        set up the third sub window -- expense window.
        '''

        # initialize the expense search window
        self.expenseSearchWindow = Toplevel()
        self.expenseSearchWindow.geometry('{}x{}'.format(600, 600))

        # initialize three stringvar to catch user's inputs
        self.stateMent = StringVar()
        self.priceRangeMent = StringVar()
        self.numMent = StringVar()

        # initialize some prompt labels
        promptLabelOne = Label(self.expenseSearchWindow, text="According to Yelp's definition, there are four categories in price ranges:")
        promptLabelTwo = Label(self.expenseSearchWindow, text="$ -- corresponding to '1' in our data, price range: under $10;")
        promptLabelThree = Label(self.expenseSearchWindow, text="$$ -- corresponding to '2' in our data, price range: $11-30;")
        promptLabelFour = Label(self.expenseSearchWindow, text="$$$ -- corresponding to '3' in our data, price range: $31-60;")
        promptLabelFive = Label(self.expenseSearchWindow, text="$$$$ -- corresponding to '4' in our data, price range: Above $61")
        promptLabelOne.place(relx=0.1, rely=0.05)
        promptLabelTwo.place(relx=0.1, rely=0.1)
        promptLabelThree.place(relx=0.1, rely=0.15)
        promptLabelFour.place(relx=0.1, rely=0.2)
        promptLabelFive.place(relx=0.1, rely=0.25)

        stateLabel = Label(self.expenseSearchWindow, text="Please input the state whose restaurants's expense range you want to see: ")
        promptLabel = Label(self.expenseSearchWindow, text="(For Example:'WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL')")
        numLabel = Label(self.expenseSearchWindow, text="Please input the numbers of top restaurants you want to see:(For Example: 5)")
        priceRangeLabel = Label(self.expenseSearchWindow, text="Please input the price range of restaurants you want to find:(For Example: 1)")

        # initialize three entries for user inputs
        stateEntry = Entry(self.expenseSearchWindow, textvariable=self.stateMent)
        numEntry = Entry(self.expenseSearchWindow, textvariable=self.numMent)
        priceRangeEntry = Entry(self.expenseSearchWindow, textvariable=self.priceRangeMent)

        stateLabel.place(relx=0.10, rely=0.33)
        promptLabel.place(relx=0.1, rely=0.38)
        stateEntry.pack()
        stateEntry.place(relx=0.10, rely=0.43)

        priceRangeLabel.place(relx=0.1, rely=0.48)
        priceRangeEntry.pack()
        priceRangeEntry.place(relx=0.1, rely=0.53)

        numLabel.place(relx=0.10, rely=0.58)
        numEntry.pack()
        numEntry.place(relx=0.10, rely=0.63)

        # initialize the show price range button
        showPriceRangeRestaurantButton = Button(self.expenseSearchWindow, text='Show Restaurant', command=self.showPriceRangeExpenseWindow)
        showPriceRangeRestaurantButton.pack()
        showPriceRangeRestaurantButton.place(relx=0.1, rely=0.69)

        # initialize the function for show price range button
        plotButton = Button(self.expenseSearchWindow, text='plot', command=self.plotRestaurantRegionExpenseWindow)
        plotButton.pack()
        plotButton.place(relx=0.65, rely=0.69)

        # initialize the clear button
        clearButton = Button(self.expenseSearchWindow, text='Clear', command=self.new_canvas_expense_window)
        clearButton.pack()
        clearButton.place(relx=0.4, rely=0.69)


    def stateStarDistributionWindow(self):
        '''
        set up the forth sub window -- overall information window.
        '''
        self.stateStarDistributionWindow = Toplevel()
        self.stateStarDistributionWindow.geometry('{}x{}'.format(600, 600))

        # initialize the star distribution button which can show the overall star distribution of six states
        starDistButton = Button(self.stateStarDistributionWindow, text='Show the Star Distribution of Six States!', command=PlotStarDistribution)
        starDistButton.pack()
        starDistButton.place(relx=0.2, rely=0.14)

        promptLabelOne = Label(self.stateStarDistributionWindow, text="Press the button to see star distribution of the six states: 'ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV' !")
        promptLabelOne.pack()
        promptLabelOne.place(relx=0.05, rely=0.08)

        meanStarDistButton = Button(self.stateStarDistributionWindow, text='Show the Mean Stars of Each State!', command=self.meanStarOfEachStateStarDistWindow)
        meanStarDistButton.pack()
        meanStarDistButton.place(relx=0.2, rely=0.26)

        promptLabelTwo = Label(self.stateStarDistributionWindow, text="Press the button to see the mean stars of the six states: 'ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV' !")
        promptLabelTwo.pack()
        promptLabelTwo.place(relx=0.05, rely=0.20)

        # initialize a select state button for user to select a certain state they want to see
        selectButtonLabel = Label(self.stateStarDistributionWindow, text='Select a button to see the pie charts for the star distribution for that state!')
        selectButtonLabel.pack()
        selectButtonLabel.place(relx=0.05, rely=0.35)

        # initialize every state's show button
        buttonON = Button(self.stateStarDistributionWindow, text='ON in Canada', command=lambda x='ON':PlotPieChartForOneState(x))
        buttonON.pack()
        buttonON.place(relx=0.2, rely=0.4)

        buttonEDH = Button(self.stateStarDistributionWindow, text='EDH in UK', command=lambda x='EDH':PlotPieChartForOneState(x))
        buttonEDH.pack()
        buttonEDH.place(relx=0.2, rely=0.52)

        buttonMLN = Button(self.stateStarDistributionWindow, text='MLN in UK', command=lambda x='MLN':PlotPieChartForOneState(x))
        buttonMLN.pack()
        buttonMLN.place(relx=0.55, rely=0.4)

        buttonWI = Button(self.stateStarDistributionWindow, text='WI in US', command=lambda x='WI':PlotPieChartForOneState(x))
        buttonWI.pack()
        buttonWI.place(relx=0.2, rely=0.64)

        buttonAZ = Button(self.stateStarDistributionWindow, text='AZ in US', command=lambda x='AZ':PlotPieChartForOneState(x))
        buttonAZ.pack()
        buttonAZ.place(relx=0.55, rely=0.52)

        buttonNV = Button(self.stateStarDistributionWindow, text='NV in US', command=lambda x='NV':PlotPieChartForOneState(x))
        buttonNV.pack()
        buttonNV.place(relx=0.55, rely=0.64)


    def checkinTimeDistributionWindow(self):
        '''
        this function is set up for checkin time distribution window
        '''

        self.checkinTimeDistributtonWindow = Toplevel()
        self.checkinTimeDistributtonWindow.geometry('{}x{}'.format(600, 600))

        self.stateEntry = StringVar()

        stateLabel = Label(self.checkinTimeDistributtonWindow, text="Please input the state whose overall restaurants' checkin numbers you want to see: ")
        promptLabel = Label(self.checkinTimeDistributtonWindow, text="You can input the following states: WI, AZ, ON, EDH, MLN, KHL, NV")
        statesEntry = Entry(self.checkinTimeDistributtonWindow, textvariable=self.stateEntry)
        stateLabel.place(relx=0.1, rely=0.25)
        promptLabel.place(relx=0.1, rely=0.3)
        statesEntry.place(relx=0.1, rely=0.35)

        # initialize the show checkin time distribution button
        showCheckinTimeDistributionButton = Button(self.checkinTimeDistributtonWindow, text='Show Checkin Time Distribution', command=self.showCheckinDistributton)
        showCheckinTimeDistributionButton.pack()
        showCheckinTimeDistributionButton.place(relx=0.1, rely=0.43)


    def showAZReviewCountsDistributionWindow(self):
        '''
        this function is set up for the state AZ's restaurants rebiew counts distribution window
        '''

        self.reviewCountsWindow = Toplevel()
        self.reviewCountsWindow.geometry('{}x{}'.format(880, 600))

        self.numberEntry = StringVar()

        promptLabelOne = Label(self.reviewCountsWindow, text="In this function, firstly, we select our all business in a given state.")
        promptLabelTwo = Label(self.reviewCountsWindow, text="Because most review records in our dataset are in state AZ, we will only look into AZ this time.")
        promptLabelThree = Label(self.reviewCountsWindow, text="Since there are too many restaurants to plot, we restrict the number of top popular restaurants to be smaller than a given threshold(say 5).")
        promptLabelFour = Label(self.reviewCountsWindow, text="We want to show you how stars given by reviewers change over time.")
        promptLabelFive = Label(self.reviewCountsWindow, text="You can input the following numbers: 1, 2, 3, 4, 5.")
        numbersEntry = Entry(self.reviewCountsWindow, textvariable=self.numberEntry)
        promptLabelOne.place(relx=0.05, rely=0.20)
        promptLabelTwo.place(relx=0.05, rely=0.28)
        promptLabelThree.place(relx=0.05, rely=0.36)
        promptLabelFour.place(relx=0.05,rely=0.44)
        promptLabelFive.place(relx=0.05, rely=0.52)
        numbersEntry.place(relx=0.05, rely=0.6)

        # initialize the show review counts distribution distribution button
        showReviewCountsDistributionButton = Button(self.reviewCountsWindow, text='Show Review Counts Distribution', command=self.showReviewCountsDistributton)
        showReviewCountsDistributionButton.pack()
        showReviewCountsDistributionButton.place(relx=0.05, rely=0.68)


    def showRestaurantSearchButton(self):
        '''
        this function is set up for the search button and its function is to search for a restaurant according to its partial name.
        '''

        mtext = self.ment.get()

        try:
            mylabel = Label(self.nameSearchWindow, text=GetUsefulInfo(NameSearch(data, mtext))[:16])
            mylabel.place(relx=0.2, rely=0.5)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(500, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, find no Restaurant of this name, please try another name.")
            inputErrorLabel.pack()


    def plot3D(self):
        '''
        this function is set up for search name window and its function is to show a 3D-figure of the distribution of stars according to the restaurants' latitude and longitude.
        '''

        mtext = self.ment.get()
        try:
            df = NameSearch(data, mtext)[:51]
            plot3dDistribution(df)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(600, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, find no Restaurant of this name so we cannot plot, please try another name.")
            inputErrorLabel.pack()


    def new_canvas_search_window(self):
        '''
        this function is set up for search restaurants window and its function is to clear the text in the window.
        '''

        w = Canvas(self.nameSearchWindow, width=500, height=500)
        w.pack()
        w.place(relx=0.2, rely=0.45)


    def showTopRestaurantsPopularWindow(self):
        '''
        this function is set up for the popular window's show top restaurants button.
        '''

        # catch user's input.
        numText = self.numMentPopularWindow.get()
        stateText = self.stateMentPopularWindow.get()

        try:
            restaurantLabel = Label(self.popularRestaurantsWindow, text=restaurantsMoreInformation(searchRestaurantByPopularity(stateText, numText))[:11])
            restaurantLabel.place(relx=0.1, rely=0.62)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(350, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input is wrong, please try again.")
            inputErrorLabel.pack()


    def new_canvas_popular_window(self):
        '''
        this function is set up for popular restaurants window and its function is to clear the text in the window.
        '''

        w = Canvas(self.popularRestaurantsWindow, width=500, height=300)
        w.pack()
        w.place(relx=0.1, rely=0.565)


    def plotTopRestaurantsPopularWinow(self):
        '''
        this function is set up for popular restaurants window and its function is to plot top restaurants.
        '''

        numText = self.numMentPopularWindow.get()
        stateText = self.stateMentPopularWindow.get()

        try:
            popularData = searchRestaurantByPopularity(stateText, numText)
            restaurantStarsPlot(popularData)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(500, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, for your input is wrong, we cannot plot now please try again.")
            inputErrorLabel.pack()


    def plotRestaurantRegionExpenseWindow(self):
        '''
        this function is set up for expense search window and its function is to plot a pie chart for the restaurants you search according to their regions
        '''

        stateText2 = self.stateMent.get()
        priceRangeText = self.priceRangeMent.get()
        numText = self.numMent.get()

        try:
            expenseData = searchRestaurantByExpenses(stateText2, priceRangeText, numText)
            restaurantRegionPlot(expenseData)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(500, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input is wrong, so we cannot plot, please try again.")
            inputErrorLabel.pack()


    def showPriceRangeExpenseWindow(self):
        '''
        this function is set up for expense search window and its function is to plot the price range of the restaurants you search
        '''

        stateText = self.stateMent.get()
        priceRangeText = self.priceRangeMent.get()
        numText = self.numMent.get()

        try:
            showPriceRangeRestaurants = Label(self.expenseSearchWindow, text=searchRestaurantByExpenses(stateText, priceRangeText, numText))
            showPriceRangeRestaurants.place(relx=0.1, rely=0.79)

        except num_topInputError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(500, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input NUMBER of top restaurants is wrong, please try again.")
            inputErrorLabel.pack()

        except stateInputError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(400, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input STATE is wrong, please try again.")
            inputErrorLabel.pack()

        except priceInputError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(400, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input PRICE RANGE is wrong, please try again.")
            inputErrorLabel.pack()

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(400, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, something else is wrong, please try again.")
            inputErrorLabel.pack()


    def new_canvas_expense_window(self):
        '''
        this function is set up for expense search window and its function is to clear the text in the window.
        '''

        w = Canvas(self.expenseSearchWindow, width=500, height=400)
        w.pack()
        w.place(relx=0.1, rely=0.74)


    def meanStarOfEachStateStarDistWindow(self):
        '''
        this function is to show the mean star of each state.
        '''

        PlotStateMeanStar()


    def showReviewCountsDistributton(self):
        '''
        this function is set up for the review counts distribution for the AZ state winodw.
        '''

        num = self.numberEntry.get()
        try:
            AZstateRestaurantReviewDistribution(num)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(400, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input number is wrong, please try again.")
            inputErrorLabel.pack()


    def showCheckinDistributton(self):
        '''
        this function is set up for the checkindistribution button and it will show a graph for the distribution.
        '''

        stateText = self.stateEntry.get()

        try:
            # check if the state is valid in our dataset
            checkin_state_check((stateText))
            plot_checkin_distribution(merge_two_df(read_business_data(), read_checkin_data()), stateText)

        # catch IO Exception
        except IOError:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(450, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, we cannot read the datafile, please check again.")
            inputErrorLabel.pack()

        except:
            errorWindow = Toplevel()
            errorWindow.geometry('{}x{}'.format(400, 30))
            inputErrorLabel = Label(errorWindow, text="Sorry, your input STATE is wrong, please try again.")
            inputErrorLabel.pack()
