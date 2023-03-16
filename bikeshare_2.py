import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
     print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago','new york city', 'washington']
        city = input("Would you like to see bikeshare data for Chicago, New York City, or Washington?").lower()
        if city in cities:
            break
        else:
            print("Please enter Chicago, New York city, or Washington")
 
    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("Which month - January, February, March, April, May, June, or all?").lower()
        if month in months:
            break
        else:
            print("Please enter a valid month.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?").lower()
        if day in days:
            break
        else:
            print("Please enter a valid day.")
 
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
  df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    map_dict = {1: "january", 2: "february", 3: "march", 4:"april", 5:"may", 6:"june"}
    df["Month"] = df["Month"].map(map_dict)
    df['Day'] = pd.to_datetime(df['Start Time']).dt.day_name()
    map_dict2 = {"Monday": "monday", "Tuesday": "tuesday", "Wednesday": "wednesday", "Thursday":"thursday", "Friday":"friday", "Saturday":"saturday", "Sunday":"sunday"}
    df["Day"] = df["Day"].map(map_dict2)
   
    #filtering by month and day
    if month != 'all':
        df= df[df["Month"]==month]
 
 
    if day != 'all':
        df = df[df['Day']==day]
   
    #display the most common month 
    if month == "all":
        common_month = df['Month'].mode()[0]
        print("The most common month for bike rental is", common_month)
   
    #display the most common day of week
    if day == "all":
        print("The most common day of the week for bike rental is", df["Day"].mode()[0])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
