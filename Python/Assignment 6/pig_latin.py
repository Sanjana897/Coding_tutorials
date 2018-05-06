"""
pig_latin.py
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/16/2017
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

to_pig_latin(word) 
-----
parameters: 
    * word - a string to be translated into pig latin
return value: a new string (in pig latin, maybe!)
description: convert a single string into pig latin; if there is more than
             word in a string (for example: "hello world"), do not 
             translate, and return the string as is

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""

def to_pig_latin(word):
    if word.isalpha() == False:
        return word
    else:
        if len(word) == 1:
            return word
        elif len(word) == 0:
            return word
        else:
            lowercase_word = word.lower()
            vowels = "aeiou"
            if lowercase_word[0] in vowels:
                lowercase_word += "way"
                return lowercase_word
            elif (lowercase_word[0] == 's' and lowercase_word[1] == 'h') or (lowercase_word[0] == 'c' and lowercase_word[1] == 'h') or (lowercase_word[0] == 't' and lowercase_word[1] == 'h') or (lowercase_word[0] == 'q' and lowercase_word[1] == 'a'):
                rearranged_word = lowercase_word[2:]
                rearranged_word += lowercase_word[0] + lowercase_word[1] + "ay"
                return rearranged_word
            else:
                rearranged_word = lowercase_word[1:]
                rearranged_word += lowercase_word[0] + "ay"
                return rearranged_word


assert to_pig_latin("u mad bro") == "u mad bro", "this test determines that words with non-alphabetic characters, including spaces, are returned as is"
assert to_pig_latin("a") == "a", "this test determines whether single-character words are returned as is"
assert to_pig_latin("") == "", "this test determins that empty strings are returned as is"
assert to_pig_latin("at") == "atway", """this test determines that words beginning with vowels have "ay" attached at the end"""
assert to_pig_latin("thimble") == "imblethay", """this test determines that words beginning with 'sh', 'ch', 'th', or 'qa' are rearranged and 'ay' is added at the end"""
assert to_pig_latin("yolo") == "oloyay", """this test determines that all other words are rearranged and 'ay' is added at the end""" 






    
