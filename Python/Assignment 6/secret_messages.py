"""
secret_messages.py
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/16/2017
=====

Write a program that encrypts a message (encodes a message so that it's 
"secret") by shifting every letter in the message a number of spaces to the
left or right. This simple encryption technique is called a Caesar Cipher:

https://en.wikipedia.org/wiki/Caesar_cipher

For example, shifting by three maps the original letters of a message to a 
letter 3 places to the right from the original letter. If there are no more 
letters to the right, continue by going back to the beginning of the alphabet. 
For a shift of three, the letters would be mapped as follows:

A → D
B → E
C → F
.
.
.
Y → B
Z → C

So... encrypting the message "ABC" would yield "DEF". A few more examples:

"Hello There" → "Khoor Wkhuh"
"Oxen and Zebra" → "Rahq dqg Cheud"

In our implementation of Casear's Cipher:

* IF A SHIFTED LETTER GOES BEYOND 'Z' or 'z', continue counting places from
  the left (that is, go back to A, and continue your shift from there)
* DO NOT SHIFT ANY CHARACTER THAT'S NOT A LETTER (retain punctuation, spaces, 
  etc.): ... with a shift of 10, "a!  b!  c!" → "k!  l!  m!"
* CASING (upper/lower case) SHOULD BE PRESERVED: shift by 1, "aRe" → "bSf"

To write this program, create 3 functions:

* encrypt - encrypt a string using Caesar's Cipher
    * input: a string to encrypt and the number of letters to shift
    * processing: use Caesar's Cipher to encrypt the string passed in based
      on the specified shift value
    * output: returns a string
* decrypt - decrypt a string using Caesar's Cipher
    * input: a string to decrypt and the number of letters that the original 
      message was shifted
    * processing: use Caesar's Cipher to decrypt the string passed in assuming
      that the original shift is the shift value passed in
    * output: returns a string
* main - contains the main logic of your program
    * input: none
    * processing: continually asks the user for input... (see specifications
      below)
    * output: does not return anything
    * remember to call main at the end of your program!

The program will:

* continually ask "(e)ncrypt, (d)ecrypt or (q)uit?" until the user enters q 
  to quit
* it should accept both upper and lowercase versions of e, d, and q
* if the user chooses encrypt
    * ask the user for a message... and how many letters to shift by
    * display the encrypted message
* if the user chooses decrypt
    * ask the user for a message... and how many letters the original message
      was shifted by
    * display the decrypted message
* hint: one way to solve this is to use chr and ord
    * what are the unicode code points of boundaries of letters?
    * check out the following chart:
      http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec
    * remember that the boundaries differ for upper and lowercase letters

Example output below:
-----

(e)ncrypt, (d)ecrypt or (q)uit?
> ???
Sorry, I can only (e)ncrypt, (d)ecrypt or (q)uit...
(e)ncrypt, (d)ecrypt or (q)uit?
> e
How many places should each letter be shifted?
> 3
What is the message?
> Hello There
Khoor Wkhuh
(e)ncrypt, (d)ecrypt or (q)uit?
> d
How many places was each letter shifted?
> 3
What was the message?
> Vhfuhw
Secret
(e)ncrypt, (d)ecrypt or (q)uit?
> e
How many places should each letter be shifted?
> -1
What is the message?
> bcd
abc
(e)ncrypt, (d)ecrypt or (q)uit?
> q
Bye!

(Optional)
Your encrypt functions probably look very similar. Try moving out the common
code into another function that both encrypt and decrypt call.
"""

def encrypt(string, shift):
    new_string = ""
    for character in string:
        if character.isalpha() == False:
            new_string += character
        else:
            #Upper case, going forward:
            if ord(character) in range (65, (91 - shift)): 
                new_character = chr(ord(character) + shift)
                new_string += new_character
            #Upper case, wrapping around:
            elif ord(character) in range ((91 - shift), 91):
                new_character = chr(ord(character) - (26 - shift))
                new_string += new_character
            #Lower case, going forward:
            elif ord(character) in range (97, (123 - shift)):
                new_character = chr(ord(character) + shift)
                new_string += new_character
            #Lower case, wrapping around:
            elif ord(character) in range ((123 - shift), 123):
                new_character = chr(ord(character) - (26 - shift))
                new_string += new_character
    return new_string


def decrypt(string, shift):
    new_string = ""
    for character in string:
        if character.isalpha() == False:
            new_string += character 
        else:
            #Upper case, going forward:
            if ord(character) in range ((65 + shift), 91):
                new_character = chr(ord(character) - shift)
                new_string += new_character
            #Upper case, wrapping around:
            elif ord(character) in range (65, (65 + shift)):
                new_character = chr(ord(character) + (26 - shift))
                new_string += new_character
            #Lower case, going forward:
            elif ord(character) in range ((97 + shift), 122):
                new_character = chr(ord(character) - shift)
                new_string += new_character
            #Lower case, wrapping around:
            elif ord(character) in range (97, (97 + shift)):
                new_character = chr(ord(character) + (26 - shift))
                new_string += new_character
    return new_string


def main():
    response = " "

    while response != "q" and response != "Q":
        response = input("(e)ncrypt, (d)ecrypt or (q)uit?\n")
        if response != "e" and response != "E" and response != "d" and response != "D" and response != "q" and response != "Q":
            print("Sorry, I can only (e)ncrypt, (d)ecrypt or (q)uit...")
        elif response == "q" or response == "Q":
            print("Bye!")
            break
        elif response == "e" or response == "E":
            shift = int(input("How many places should each letter be shifted?\n"))
            message = input("What is the message?\n")
            if shift >= 1:
                print(encrypt(message, shift))
            elif shift <= 1: #In case user enters negative shift, should decrypt but with absolute value
                print(decrypt(message, abs(shift))) 
        elif response == "d" or response == "D":
            shift = int(input("How many places was each letter shifted?\n"))
            message = input("What is the message?\n")
            if shift >= 1:
                print(decrypt(message, shift))
            elif shift <= 1: #In case user enters negative shift, should encrypt but with absolute value
                print(encrypt(message, abs(shift)))
        
main()



