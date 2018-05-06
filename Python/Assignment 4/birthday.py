"""
birthday.py
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/05/2017
Assignment instructions: https://foureyes.github.io/csci-ga.1120-fall2017-001/assignments/hw04.html
"""

import mydate
import listutils

simulation_repeats = int(input("How many times should I run the simultation?\n"))
num_birthdays = int(input("How many birthdays should I generate per trial?\n"))
trials_with_duplicates = 0

for i in range(0, simulation_repeats):
    duplicate_birthday_string = ""
    generated_dates = []
    for j in range(0, num_birthdays): 
        generated_dates.append(mydate.generate_date(1916, 2016)) 

    mydate.remove_years(generated_dates) 

    duplicate_birthdays = listutils.finding_duplicates(generated_dates)  
    if duplicate_birthdays == []:
        print("Trial %i: No dates are the same" %(i+1))
    else:
        trials_with_duplicates +=1
        for k in duplicate_birthdays:
            month = mydate.month_num_to_string(k[0])
            if duplicate_birthdays.index(k) == (len(duplicate_birthdays)-1):
                duplicate_birthday_string += month + " " + str(k[1])
            else:
                duplicate_birthday_string += month + " " + str(k[1]) + ", "
            
        print("Trial %i: %i dates occur more than once! (%s)" %(i+1, (len(duplicate_birthdays)), duplicate_birthday_string))
    
print("Results:")
print("Out of %i trials, %i had dates that were repeated" %(simulation_repeats, trials_with_duplicates))
probability = str((trials_with_duplicates*100)/simulation_repeats) + "%"
print("We can conclude that you have a %s chance of sharing a birthday with someone if you are in a group of %i people" %(probability, num_birthdays))
