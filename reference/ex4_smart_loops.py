# You are given a list of years in which people were born
#
# Use variables, for loops, and if statements to complete the following tasks

birth_years = [2002, 1985, 2007, 1963, 1982, 1976,
               2006, 2010, 1994, 1992, 1971, 1994, 2000, 1991,
               1961, 1984, 2003, 2006, 1998, 1981, 1962, 2007]

# change current year as needed
current_year = 2018

# Task 1: count how many people are more than (hint: greater than) 50 years old
#
# ex: if you were born in 1990, and the current year is 2018, then
# subtracting 1990 from 2018 gives us 28 years.

count_1 = 0
# for every year
for year in birth_years:
    # age is current year - given year
    age = current_year - year
    # is the difference in years greater than 50?
    if age > 50:
        # then add 1 to our count variable
        count_1 = count_1 + 1

print('There are '+ str(count_1) + ' people over 50 in this list.')

# Task 2: count how many people are more than (hint: greater than)
# 20 years old and less than 30 years old

count_2 = 0
# for every year
for year in birth_years:
    # age is current year - given year
    age = current_year - year
    # is the age greater than 20 and is the age less than 30?
    if age > 20 and age < 30:
        # then add 1 to our count variable
        count_2 = count_2 + 1

print('There are '+ str(count_2) + ' people between ages 20 and 30 in this list.')

# Bonus: what is the average age of this list of people?
count_3 = 0
sum_3 = 0
# for every year
for year in birth_years:
    # add 1 to our count variable
    count_3 = count_3 + 1
    # add the year to our sum variable
    sum_3 = sum_3 + year

# the average (mean) is sum divided by count
avg_year = sum_3 / count_3
# age (again) is current year - given year
avg_age = current_year - avg_year

print('The average age of this list of people is '+ str(avg_age) + ' years old.')
