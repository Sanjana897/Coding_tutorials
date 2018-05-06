"""
is_palindrome.py (4 points)
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/16/2017
=====

Determine whether or not a string is a palindrome.

http://en.wikipedia.org/wiki/Palindrome 

For our purposes, strings that are palindromes are strings that are the same 
backwards and forwards.  Some examples of palindromes include:

"racecar"
"straw warts"
"ABBA"

For this assignment, write two functions:

1. reverse(s)
   a. reverses the order of the characters in a string...
   b. takes a string as an argument
   c. returns a new string with the letters of the original reversed
   d. "hello" would return "olleh"
   e. "" returns ""
   f. write at least two assertions for this
2. is_palindrome(s)
   a. determines whether or not the supplied string is a palindrome
   b. takes a string as an argument
   c. returns a boolean value: True if the string is a palindrome, False 
      otherwise
   d. use the above reverse function to help determine whether it is a
      palindrome or not
   e. write at least two asssertions (one for a True case and one for a False
      case)
"""

def reverse(string):
    reversed_word = ""
    for i in range(len(string), 0, -1):
        reversed_word += string[i-1]
    return reversed_word

assert reverse('hello') == 'olleh', "this test determines if the word is getting reversed"
assert reverse('') == '', "this test determines whether a blank string returns a blank string"

def is_palindrome(s):
    if reverse(s) == s:
        return True
    else:
        return False

assert is_palindrome('hello') == False, "returns False if the word is not a palindrome"
assert is_palindrome('level') == True, "returns True if the word is a palindrome"
    
