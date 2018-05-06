"""
mydate.py
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/05/2017
Assignment instructions: https://foureyes.github.io/csci-ga.1120-fall2017-001/assignments/hw04.html
"""

def is_valid_month_num(n):
    if n > 0 and n < 13:
        return True
    else:
        return False


def month_num_to_string(month_num):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if is_valid_month_num(month_num) == True:
        month_string = month_list[(month_num-1)]
        return month_string
    else:
        return None

def date_to_string(date_list):
    date_list[1] = month_num_to_string(date_list[1])
    date_string = "%s %i, %i" % (date_list[1], date_list[2], date_list[0])
    return date_string
  
def dates_to_strings(list_of_date_lists):
    list_of_date_strings = []
    for element in list_of_date_lists:
            element = date_to_string(element)
            list_of_date_strings.append(element)
    return list_of_date_strings

def remove_years(list_of_date_lists):
    list_without_year = []
    for element in list_of_date_lists:
        element.pop(0)
        list_without_year.append(element)
    return list_without_year

def is_leap_year(year):
    if year % 4 == 0:
        checkpoint = True
        if year % 100 == 0 and year % 400 != 0:
            checkpoint = False
    else:
        checkpoint = False
    return checkpoint
            
          
def get_num_days_in_month(month_num, year):
    if is_valid_month_num(month_num) == False:
        return None
    else: 
        if is_leap_year(year) == True:
            days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_given_month = days_per_month[(month_num-1)]
        return days_in_given_month

def generate_date(start_year, end_year):
    import random
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, get_num_days_in_month(month, year))
    random_date = [year, month, day]
    return random_date
    








    
