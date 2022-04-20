"""
The Cosmic Calculator is used to convert from millions of years to a calendar date time. It is used to place notable events on Carl Sagan's Cosmic Calander (the timespan of the universe fit accross one calendar year)
"""
from datetime import datetime, timedelta
from math import modf

age_of_universe = 13797000000  # in years

days_in_year = 365

years_in_cosmic_day = age_of_universe / days_in_year

years_ago = float(
    input(
        'Enter how long ago the event occured in millions of years. For example, "10.1" = 1,100,000 years.\n'
    )
) * 1000000

cosmic_days_decimal = years_ago / years_in_cosmic_day

cosmic_hours_decimal = cosmic_days_decimal * 24

cosmic_hour_remainder_decimal, cosmic_hours = modf(cosmic_hours_decimal)

cosmic_minutes_decimal = cosmic_hour_remainder_decimal * 60

cosmic_minute_remainder_decimal, cosmic_minutes = modf(cosmic_minutes_decimal)

cosmic_seconds_decimal = cosmic_minute_remainder_decimal * 60

cosmic_seconds = round(cosmic_seconds_decimal)

new_year_date = datetime(year=2022, month=1, day=1)

cosmic_difference = timedelta(
    hours=cosmic_hours,
    minutes=cosmic_minutes,
    seconds=cosmic_seconds
)

cosmic_datetime = new_year_date - cosmic_difference

print(str(cosmic_datetime))
