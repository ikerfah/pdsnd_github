
import time
import pandas as pd
import numpy as np



# To keep . the same pattern as CITY_DATA
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_OF_WEEK_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("Please select a city [chicago, new york city, washington] : ")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("You probably made a typo, Please check city's name again and it's must be one of [chicago, new york city, washington] \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("Please select a month [all, january, february, march, april, may, june] : ")
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
        else:
            print("You probably made a typo, Please check month's name again.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_OF_WEEK_DATA:
        day_name = input("Please select a day of week [all, monday, tuesday, wednesday, friday, saturday, sunday] : ")
        if day_name.lower() in DAY_OF_WEEK_DATA:
            day = day_name.lower()
        else:
            print("You probably made a typo, Please check day of month's name again.\n")

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
    df = pd.read_csv(city)

    # Source : https://stackoverflow.com/questions/53234770/filtering-pandas-dataframe-by-day
    # we should use pandas datetime and not python
    # Source : This one from Practice Solution #3 udacity
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
#     we need this later, it's not required here
    df['hour'] = df['Start Time'].dt.hour


    # Here wi filter by month if user select something differnt from all
    if month != 'all':
        # Convert string to index , because our dataframe contains month index and not str
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]

    # Here wi filter by day of month if user select something differnt from all
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    # here we get only the filtred dataframe and we are ready to go
    # print(df.head()) to show first 5 rows and we can check if our filter is applicable     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('------- Popular times of travel -------')
    # TO DO: display the most common month
    # Series.mode : Return the highest frequency value in a Series     
    # source : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html     
    common_month = df['month'].mode()[0]
    print("Most common month: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("most common day of week: " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    
    # str() which will convert the argument passed in to a string format
    print("most common hour of day: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('------- Popular stations and trip -------')
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("most common start station: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("most common end station: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("most common trip from start to end (i.e., most frequent combination of start station and end station) : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('------- Trip duration -------')
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data step by step on user's need.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    # show 5 top rows  , Head by default param 5
    # Source : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html     
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('Would you like to view next five rows ? [y/n] : ')
        if view_raw_data.lower() != 'y':
            return
        next = next + 5
        # Series.iloc Purely integer-location based indexing for selection by position.         
        # Source : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html         
        print(df.iloc[next:next+5])
        
def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('------- User info -------')

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of each user type: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("counts of each gender: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth : {}\n'.format(earliest_birth))
        print('Most recent birth : {}\n'.format(most_recent_birth))
        print('Most common birth : {}\n'.format(most_common_birth) )

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
        # This is from the project description , Use descriptive statistics to answer questions about the data. Raw data is displayed   upon request by the user.
        while True:
            raw_data = input('Would you like to view next five (5) rows from the result? [y/n] : ')
            if raw_data.lower() != 'y':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? [yes/no] [y/n]')
        if restart.lower() != 'y' and restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
