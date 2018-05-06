"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 10/31/2017
myster_solved.py
=====

Given the coded (encrypted) text in secret.py, find out what book and 
author the text comes from. It is encoded by substituting one letter for 
another.

Consequently, it's possible to decode some of the text by using letter 
frequency analaysis.

First, read the following for some background material:
-----
1. Sorting using sorted: https://docs.python.org/3/library/functions.html#sorted
2. An explanation of using sorted: test_ordering.py (on the course site)
3. Letter frequencies: http://norvig.com/mayzner.html

To decode the text in secret.py:
-----
1. in this file, import secret... the variable, secret.text, will 
   contain the encoded text; feel free to print it out to view it!
2. calculate the number of times each letter occurs in the encrypted 
   text; there are some tricky things that might have to be dealt with:
    * what should you do with non-letter characters?
    * how should casing be handled?
3. print out the letters and their counts in descending order based on 
   count
4. using your calculations and the freqency of letters given by the site 
   above (http://norvig.com/mayzner.html gives us these letters in order
   of descending frequency... 'etaoinsrhldcumfpgwybvkxjqz')
5. ...come up with a mapping: for example, your most frequently occurring 
   letter will map to 'e', the 2nd most frequently occurring will map to 
   't'
6. print out the mapping
7. go through the original encoded text, and substitute the letters 
   appropriately based on frequency
8. finally, display a semi-translated version of the text!

Requirements
-----
1. print out letters and their counts from the encoded text
2. print out your mapping of what letters should be substituted (for 
   example if all x's in the original text should be substituted with e, 
   then print out something like: x -> e)
3. print out a semi-decoded version of the encoded text
4. you must use a dictionary or dictionaries somewhere in your code
5. lastly, in a comment above your code, write a short description of 
   the process that you used and your guess for the source book and author

You can create any functions or modules you want to do this.
"""

import secret

#Creating a dictionary with frequencies
#Only taking alphabets, ignoring other characters
#Converting all letters to lower case
    #to avoid upper and lower case letters getting counted separately
def finding_frequency(text):
    letter_frequencies = {}
    for letter in text:
        if letter.isalpha() == False:
            continue
        else:
            lower_case_letter = letter.lower()
            letter_frequencies[lower_case_letter] = letter_frequencies.get(lower_case_letter, 0) + 1
    return letter_frequencies


#Creating a list with the reverse sorted keys (sorting by values)
#Using that to key into the dictionary and printing values
def reverse_sorting_list(text):
    letter_frequencies = finding_frequency(text)
    reverse_sorted_values = sorted(letter_frequencies, key = letter_frequencies.get, reverse=True)
    return reverse_sorted_values


#Printing the reverse sorted list
#I put this in a separate function so that printing it is optional
def print_reverse_sorted_values(text):
    reverse_sorted_values = reverse_sorting_list(text)
    letter_frequencies = finding_frequency(text)
    for frequency in reverse_sorted_values:
        print(frequency, letter_frequencies[frequency])

print_reverse_sorted_values(secret.text)

#Generating a dictionary with mapped values
def mapping(text):
    reverse_sorted_values = reverse_sorting_list(text)
    frequency = "etaoinsrhldcumfpgwybvkxjqz"

    mapped_dictionary = {}
    for i in range(len(reverse_sorted_values)):
        mapped_dictionary[reverse_sorted_values[i][0]] = frequency[i]
    return mapped_dictionary


#Printing out the mapped dictionary
#I put this in a separate function so that printing it is optional
def print_mapping(text):
    mapped_dictionary = mapping(text)
    for i in mapped_dictionary:
        print(("{0} --- {1}".format(i, mapped_dictionary.get(i))))

print_mapping(secret.text)


#Translating the passage
#Accumulating the translated text in a new string
#Checking whether it's upper case
    #if so, using the lower case version of the letter as the key to the dictionary
    #and then adding the upper case version of the value to the new string
#Adding special characters to the new string as is
def translating_text(text):
    mapped_dictionary = mapping(text)
    translated_text = """"""
    for character in text:
        if character.isalpha():
            if character.isupper():
                mapped_character = mapped_dictionary.get(character.lower())
                translated_text += mapped_character.upper()
            else:
                translated_text += mapped_dictionary.get(character)
        else:
            translated_text += character
    return translated_text
        
print(translating_text(secret.text))       

#Book seems to tbe The Last Man, by Mary Wollstonecraft Shelley
