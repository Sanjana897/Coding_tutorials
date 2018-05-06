#Class 6

#If string formatting placeholders and values don't line up, error:
#“Substitute %s, %s and %s” %(this) Too few
#“Substitute %s, %s and %s” %(this, this, this, that) Too many

#Lists are mutable; can replace values
names = ['alice', 'bob', 'carol']
names[0] = 'eve'
print(names)

#Can’t do in strings:
s = 'hello'
#s[0] = ‘c’   Error. Strings are immutable. 

s += ' world' #is allowed, because it technically doesn’t change the string, creates a new one. 

#For loops and strings, goes through every character, prints each one
my_crazy_string = "oh, my!"
for c in my_crazy_string:
  print(c)

#Another for loop and string, prints each character with the suffix 'am'
word = "jetpack"
suffix = "am"
for c in word:
	print(c + suffix)

#Get the first word of a sentence
#Assuming that words are separated by spaces (not dashes, colons, semi colons, etc.)
#If string is empty os has no spaces, should return as is
#Method 1: Slicing
def get_first_word(sentence):
    if sentence.count(" ") == 0:
        return sentence
    else:
        space_index = sentence.index(" ")
        first_word = sentence[:space_index] #If you don't specify start, assumes 0
        return first_word

#Method 2: Accumulating during for loop
def get_the_first_word(sentence):
    word = ''
    for i in sentence:
        if i != ' ':
            word += i
        else:
            break
    return word

#Method 3: Slicing without index
def find_first_word(sentence):
    add_last_letter = True #Have to add this complication because last letter was getting cut off
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            add_last_letter = False
            break
    if add_last_letter: #Same as above
        return sentence[0:i+1] 
    else:
        return sentence[0:i]

print(find_first_word('hahah'))

#Method 4: Find and count
def get_the_first_word(sentence):
    if sentence.count(" ") == 0:
        return sentence
    else:
        first_word = sentence[:sentence.find(" ")]
        return first_word

print(get_the_first_word("hi"))
    

#Function that checks if a letter is in a word, returns True or False
def letter_in_word(letter, word):
    for character in word:
        if character == letter:
            return True
        else:
            return False
#This works for c, works for x. Doesn't work for a. Because loop stops after c, due to return, which stops function.

def letter_in_word(letter, word):
    for character in word:
        if character == letter:
            response =  True
        else:
            response = False
        return response
#This works for c, works for x. Doesn't work for a. Not sure why

#Way around is to not use else. Set value before loop, change if it finds 
def letter_in_word(letter, word):
    result = False
    for character in word:
        if character == letter:
            result = True
            break
    return result
print(letter_in_word('a', 'cat'))

#Function that removes vowels from a word
#Hint: Can't change original string, accumulate in new one
#Make it fancy: Upper and lower case, second parameter asking if y is a vowel
def remove_vowels(word):
    new_word = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] #Can do this as a string instead of list, will work the same 
    for i in word:
        if i not in vowels:
            new_word += i
    return new_word

print(remove_vowels('HIya'))
    
#Can also retrieve a substring from a string, by slicing
word = "banana"
ana = word[3:]
print(ana)


#Check whether every character in a string is a digit
#Use in not in to compare to a string to digits "1234567890"
def is_digit(string):
    digits = "1234567890"
    for i in string:
        if i not in digits:
            return False
        else:
            continue
    return True
            
print(is_digit('jjj'))
print(is_digit('123'))

#Food is the object, .upper() is the method
food = "pizza"
print(food.upper())

#Casing methods
print("this should be uppercase".upper())
print("THIS SHOULD BE LOWERCASE".lower())
print("the first word should be uppercase".capitalize())
print("first word of each sentence should be title case".title())


#isdigit(), isnumeric() and isalpha()
print("123".isdigit())            # True
print("1.23".isdigit())           # False (. is not 0 - 9)
print("one two three".isdigit())  # False (not 0 - 9)
print("onetwothree".isalpha())    # True
print("one two three".isalpha())  # False (has spaces)
print("one!".isalpha())           # False (has !)
print("1".isalpha())              # False (it's a digit)
print("⅕".isdigit())              # False (not 0 - 9)
print("⅕".isnumeric())            # True (isnumeric allows other numeric chars)

#isspace(), checks for tabs, carriage returns and spaces
print("             ".isspace()) #True
print("\n".isspace()) #True
print("\t".isspace()) #True. \t is tab
print("some    space".isspace()) #False. Has characters, so not purely space

#strip, removes leading and trailing white space
print("  spaces all around   ".strip())

#Format
print("{0} elephants".format("twenty"))
print("{0} elephants".format(20))
print("{0} elephants".format(20, 100)) #Invoking index 0
print("{1} elephants".format(20, 100)) #Invoking index 1
print("{0} elephants and {1} peanuts".format(20, 100)) #Using both
print("{1} elephants and {1} peanuts".format(20, 100)) #Using only the 100 twice, string formatting doesn't allow you to do this, have to make both values 100.

#More on format, template is a variable
template = "{} my name is {}" #If you don't put index, takes them in order
print(template.format('hello', 'joe'))

#template = "{2} my name is {1}"
#print(template.format('hello', 'joe'))
#This doesn't work because the index starts at 0, and there is nothing in index 2

#Can use them in any order
template = "{1} my name is {0}" 
print(template.format('hello', 'joe')) 

#Can use them multiple times
template = "{1} my name is {0} {1}" 
print(template.format('hello', 'joe'))

#Can substitute with variables
template = "{greeting} my name is {name}" 
print(template.format(greeting='hello', name='joe'))

#Can assign variable to another variable
t = 'hola' 
print(template.format(greeting=t, name='joe'))

#Can use variable multiple times
template = "{greeting} {greeting} my name is {name}" 
print(template.format(greeting=t, name='joe'))

#Can't do this kind of assignment, error
greeting='hola'
#print(template.format(greeting, name='joe')) 

#Can do other operations
print(template.format(greeting=t * 3, name='joe'))

#count counts the number of times a substring occurs in the original string
print('aardvark'.count('a')) 

#replace replaces instances of substring with another, gives back new string, doesn't mutate the old
print('aardvark'.replace('a', '42'))

#Have a forever loop, ask user if they want to stop, stop it only if they say yes
#Use upper, lower, capitalize and title to check all the versions of yes, any are allowed
stop_word = "yes"
while True:
    response = input("Do you want this to stop?\n")
    if response == stop_word or response == stop_word.upper() or response == stop_word.capitalize() or response == stop_word.title():
        break
    else:
        continue

#split gives back list of each of these words, splits on each comma
x = 'blue,red,green'
print(x.split(','))

#Can do using space, or any other character or letter
words = 'This is random text we’re going to split apart'
words2 = words.split(' ')
print(words2)

#join joins the elements of a list, into a string
list = ["hello", "hi", "goodbye"]
print("xx".join(list)) #xx is the glue

#can join using space as the glue
list = ["hello", "hi", "goodbye"]
print(" ".join(list)) #xx is the glue

#ord gives the Unicode point (integer value) of the character supplied
print(ord('c')) #99
print(ord('C')) #67
print(ord('.')) #46

#chr gives the character represented by the supplied code point
print(chr(55)) #7
print(chr(70)) #F



