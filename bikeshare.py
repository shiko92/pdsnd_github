import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
    # TO DO: make a Dict for the 3 files that will be used through the project

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("choose a city from the following: Chicago, New York, washington \n" ).lower()
        if city.lower() not in ('chicago', 'new york', 'washington'):
            print("Not an appropriate choice.")
        else:
            break
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("January, February, March, April, May, June or All \n" ).lower()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Not an appropriate choice.")
        else:
            break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Monday, Sunday, Tuesday, wednesday, Thursday, Friday, Saturday or All \n" ).lower()
        if day.lower() not in ('monday', 'sunday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all' ):
            print("Not an appropriate choice.")
        else:
            break

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    x = 'Gender' in df.columns
    print (x)
    if 'Gender' in df.columns :
        df['Gender'] = df['Gender'].fillna('Unknown')


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        # filter by month to create the new dataframe
        df = df[df['month'] == month]



    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    df['month'] = df['Start Time'].dt.month
    month_counts = df['month'].value_counts()
    while (month_counts.size > 1):
        popular_month = df['month'].mode()[0]
        print('the most common month is:', popular_month)
        break;


   # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    day_counts = df['day_of_week'].value_counts()
    while (day_counts.size > 1):

        popular_day = df['day_of_week'].mode()[0]
        print('the most common day is:',popular_day)
        break;


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common hour is:',popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].value_counts().index.tolist()[0]
    pop_start_station_count = df['Start Station'].value_counts()[0]
    print('most commonly used start station:{}, with total counts of {}'.format( pop_start_station, pop_start_station_count ))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].value_counts().index.tolist()[0]
    pop_end_station_count = df['End Station'].value_counts()[0]
    print('most commonly used end station:{}, with total counts of {}'.format( pop_end_station, pop_end_station_count ))

    # TO DO: display most frequent combination of start station and end station trip
    pop_start_end_station = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print('most frequent combination of start station and end station trip:{}'.format(pop_start_end_station))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_seconds = df['Trip Duration'].sum()
    print('total travel time is: {} seconds.'.format(total_travel_seconds))


    # TO DO: display mean travel time
    mean_travel_seconds = df['Trip Duration'].mean()
    print('mean travel time is: {} seconds.'.format(mean_travel_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        user_types = df['Gender'].value_counts()
        print(user_types)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest_birth_year =int( df['Birth Year'].min())
        print(earliest_birth_year)
        recent_birth_year = int(df['Birth Year'].max())
        print(recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print(common_birth_year)


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




        while True:
            raw_data = input('\nWould you like to see some raw data? Enter yes or no.\n')
            # TO DO: asks if user want a sample of row data
            if raw_data.lower() == 'yes':
                random_or_specific_rows = input('\nIf you would like to see random data rows press 1 for specific rows Enter 2.\n')
            # TO DO: asks if user want to see random or specific row  data
                if random_or_specific_rows  == '1':
                    rows_number = int(input('\nHow many rows you would like to preview ? please Use Integrs numbers only!! \n'))
                    print(df.sample(n = rows_number))
            # TO DO: asks how many rows user want to see
                elif random_or_specific_rows  == '2':
                    start_row_number = int(input('\nEnter start row number, please Use Integrs numbers only!! \n'))
            #TO DO: asks user for the start row
                    end_row_number = int(input('\nEnter end row number, please Use Integrs numbers only!! \n'))
            #TO DO: asks user for the end row
                    print(df.iloc[start_row_number : end_row_number])

                elif random_or_specific_rows  not in ('1','2'):
                    print('Not an appropriate choice.')
                    # force user to enter valid inputs 
                continue
            else:
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
