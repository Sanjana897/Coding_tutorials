"""
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 09/18/2017
"""

"""
multiply.py 
=====
Write a program that:

* asks the user for a number
* prints out a table of that number multiplied by the first 7 prime numbers:  
  2, 3, 5, 7, 11, 13, 17
* it will format the output so that the original number and the prime number are
  left aligned
* the product is right aligned
  * when using format, don't change the width to align the product
  * keep the width constant
* __COMMENT YOUR SOURCE CODE__ by 
   * briefly describing parts of your program 
   * include your name, the date, and your class section at top of your file 
     (above everything else)

Example interaction (everything after > is user input):
-----
Give me a number
> 17
17 * 2             34
17 * 3             51
17 * 5             85
17 * 7            119
17 * 11           187
17 * 13           221
17 * 17           289
"""

#Defining variables
number_string = input('Give me a number\n')
number_int = int(number_string)

#Printing out table
print(format(number_string + ' * 2', '<15s'), format(str(number_int*2), '>15s'))
print(format(number_string + ' * 3', '<15s'), format(str(number_int*3), '>15s'))
print(format(number_string + ' * 5', '<15s'), format(str(number_int*5), '>15s'))
print(format(number_string + ' * 7', '<15s'), format(str(number_int*7), '>15s'))
print(format(number_string + ' * 11', '<15s'), format(str(number_int*11), '>15s'))
print(format(number_string + ' * 13', '<15s'), format(str(number_int*13), '>15s'))
print(format(number_string + ' * 17', '<15s'), format(str(number_int*17), '>15s'))

#Note: Seems like this program would have been easier with the % string formatting command! 
