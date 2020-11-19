import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago, new york city, washington: ').lower()
    while city in ['chicago', 'new york city', 'washington']:
        break
    else:
        print('This is not a valid input, please reenter the city name')
        city = input('Would you like to see data for chicago, new york city, washington: ').lower()

            
    Filter = input('Would you like to filter the data by month, day, both or not at all, please type (none for no filter): ')
    
    while Filter in ['month', 'day', 'both', 'none']:
        break
    else:
        print('This is not a valid input, please reenter the filter')
        Filter = input('Would you like to filter the data by month, day, both or not at all, please type (none for no filter): ')
    
    
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if Filter == 'month':
        day = None
        month = input('Which month? January, Febreuary, March, April, May, or June, please type out the full month name: ').lower()
        
        while month in months:
            break
        else:
            print('This is not a valid input, please reenter the month')
            month = input('Which month? January, Febreuary, March, April, May, or June, please type out the full month name: ').lower()
        
    elif Filter  == 'day':
        month = None
        day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday, please type out the full day name: ').lower()
        
        while day in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
            break
        else:
            print('This is not a valid input, please reenter the day')
            day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday, please type out the full day name: ').lower()

        
    elif Filter == 'both':
        
        month = input('Which month? January, Febreuary, March, April, May, or June, please type out the full month name: ').lower()
        day = input('Which day? saturday, sunday, Monday, Tuesday, Wedbesday, Thursday, or Friday, please type out the full day name: ').lower()
    
        while (month in months) & (day in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']):
            break
        else:
            print('Invalid input, please reenter')
            
            month = input('Which month? January, Febreuary, March, April, May, or June, please type out the full month name: ').lower()
            day = input('Which day? saturday, sunday, Monday, Tuesday, Wedbesday, Thursday, or Friday, please type out the full day name: ').lower()

    elif Filter == 'none':
        month = None
        day = None

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != None:
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if (day != 'all') & (day != None):
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month_num = df['month'].mode()[0]
    popular_month_name = months[popular_month_num - 1]
    print('the most common month is: {}'.format(popular_month_name))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0].title()
    print('the most common day of week is: {}'.format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common hour is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most common start station is: {}'.format(popular_start_station))
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most common end station is: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('the most common combination of start and end station is: {} and {}'.format(popular_combination[0], popular_combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {}'.format(total_travel_time))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {}'.format(mean_travel_time))   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        
        print(gender)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        recent_yob = df['Birth Year'].max()
        common_yob = df['Birth Year'].mode()[0]
        print('Earliest year of birth is {}, most recent year of birth is {}, most common year of birth is {}'.format(earliest_yob, recent_yob, common_yob))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
