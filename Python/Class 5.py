#Class 5
"""
#Docstrings, the first comment under the function shows up when you get help on that function
def foo(bar):
    """'foo will print out the argument passed in'"""
    print(bar)
help(foo)

#Using assert to test. This code doesn't work
def is_short_string(stringg):
    return len(stringg) < 3
    #return True

assert is_short_string('hello') == False, "this test determines if function returns false if we have a long string"
assert is_short_string('') == True, "returns true if string is less than 3 chars"

#Return: None
result = print('hello') #Will print hello because print function was called
print(result) #Will print None because print doesn’t return anything.

#If you don’t define a return value for the function, it will give back none:
def foo():
    s = "bar"
    # no return 

result = foo()
print(result) #None

#Slicing lists
cats = ['chairman meow', 'heathcliff', 'paw newman', 'kitty purry']
expensive_cats = cats[0:3] #Takes those values and adds them to a new list
print(cats) #Original list stays the same
print(expensive_cats)
cats = cats [1:3]
print(cats) #Original list gets sliced

#The index method gives back the position of an item in the list
print(cats.index('paw newman'))
#print(cats.index('animal')) If the item doesn’t exist in the list it gives an error. 

cats.append('chairman meow')
print(cats)

#Pop takes off a value. One of the few list methods to return a value
cats.pop(0) #Takes off first value
print(cats)

cats.pop() #If you don't specify which, takes off the last one
print(cats)

animals = [cats, ['bark twain', 'jane pawsten']] #2 lists within a list
for lst in animals: #To print out each element (and not the two lists), need to use a nested list
    for ele in lst:
        print(ele)

print(animals[1][0]) #Can also be used to print elements from the inner list

#The list function
print(list(range(5))) #If you pass in a range, gives you all the numbers
print(list("string")) #If you pass in a string, gives you all the letters
empty_list = []
print(list(empty_list)) #If you have a blank list, gives you back empty brackets
print(list(animals)) #If you pass in a list, gives you the elements


colors = ['blue', 'puce', 'dusty rose', 'fuscia']
#One way to change is with for color in colors
#Another is by changing things in the list based on index. This changes the original list.
for i in range(len(colors)):
    print(i) #Prints the numbers

#Changing the original list based on position
print('before', colors)
for i in range(len(colors)):
    colors[i] = colors[i] * 2
print('after', colors)

#Print out index + value
for i in range(len(colors)):
    print(i + 1, colors[i])

#If you assign something new to the loop variable, it doesn’t change the actual list. Unless you use the list index. 
for c in colors:
    c = c * 2 #c is reassigned within the loop
    print(c)
print(colors) #Remains the same

"""
"""
#Global vs local variables within functions
snake = 'hissy elliot' #Global variable
def shout():
    snake = snake + "!" #Trying to reassign locally but gives an error
    #Trying to assign snake locally (LHS) but finds snake on RHS and doesn't know what it is
    #Local assignment is incomplete
    print('in function', snake)
shout()
print('out of function', snake)
"""
"""

#But if the global variable is mutable, like a list, can change it from within a function.
characters = ['yt', 'hiro protagonist', 'raven']
def remove_first():
    characters.pop(0) #Delete first value
    print(characters)
    characters[0] = 1 #Change hiro protagonist to 1
    print(characters)
remove_first()
print(characters) #Entire list has changed

#Pop doesn’t return a value if it’s in a function that doesn’t return the value. 
characters = ['yt', 'hiro protagonist', 'raven']
def remove_first(lst):
    lst.pop(0)
print('before', characters)
result = remove_first(characters)
print(result) #Gives none, because return isn't specified
print('after', characters)

#If use pop with return, then it gives a value
characters = ['yt', 'hiro protagonist', 'raven']
def remove_first(lst):
    return lst.pop(0)
print('before', characters)
result = remove_first(characters)
print(result) #Gives the value that was popped off
print('after', characters)


#Double every number in a list and put all the values in a new list
#Known as mapping. Taking every element in a list, transforming it and putting it in a new one
#Don't hard code the list into the function, can't use it on another function
#Put the list in as a parameter. Makes function reusable
num = [10, 15, 3, 9]
doubled_num = []

def double_the_number (original_list):
    for number in original_list:
        doubled = number * 2
        doubled_num.append(doubled)
    return doubled_num #If this is in the loop it stops the loop after the first value

double_the_number(num)
print(doubled_num) #Can put the print command in the function, after return. But suppose you don't want to print, want to do something else with the value? 

double_the_number([2,5,8])
print(doubled_num)

#---------------------------------------------

#Take a list of numbers and give back a new list of numbers with only the even ones
numerals = [5, 8, 144]
evens = []

def finding_evens(initial_list):
    for i in initial_list:
        if i % 2 == 0:
            evens.append(i)
    return evens

finding_evens(numerals)
print(evens)

#---------------------------------------------

#Instead of putting the calculation in the program, can make it another function:
def is_even(n):
    return n % 2 == 0

def get_even_numbers(digits):
    filtered_list = []
    for j in digits:
        if is_even(j): #Takes everything after the word return in the above function and puts it here
            filtered_list.append(j)
    return filtered_list

list_of_numbers = [2,3,4,5,6]
print(get_even_numbers(list_of_numbers))
            
#---------------------------------------------

#Enumerate: Idiomatic way of getting indexes in Python
#Use enumerate on a list, it gives you tuples of element and index:
bands = ['lil yachty', 'migos', 'outkast', '21 savage']
for i, ele in enumerate(bands):
    print(i, ele) #Output: 0 lil yachty

#Can also use it with the list function:
print(list(enumerate(bands))) #Output: [(0, 'lil yachty'), (1, 'migos'), (2, 'outkast'), (3, '21 savage')]

for t in enumerate(bands):
    print(type(t), t) #Prints the type and enumerates the index and value: <class 'tuple'> (0, 'lil yachty')

for t in enumerate(bands):
    i, ele = t
    print("%s - %s" % (i, ele)) #Prints them in a 0 - lil yachty format

#---------------------------------------------

#Concatenation doesn't actually change the original list:
numbers = [1, 2, 3, 2, 2, 2]
print(numbers + [1, 2])
print(numbers) #Original list is the same

#Sorts in order
numbers.sort()
print(numbers)

#Reverses order of the elements
numbers.reverse()
print(numbers)

#List comprehension basic syntax. Copies the exact same list
a = [1, 2, 3]
new_list = [n for n in a]
print(new_list)

#List comprehension: Mapping. Make a new list that multiplies all the numbers in numbers by 2:
new_numbers = [n * 2 for n in numbers]
print(new_numbers)

#List comprehension: Filtering. Make a new list with even elements from numbers
new_numbers = [n for n in numbers if n % 2 == 0]
print(new_numbers)

#Can change the case, add if condition to filter:
words = ['this', 'is', 'a', 'list'] 
print([w.upper() for w in words if len(w) > 2]) #Instead of printing, can assign to variable to save

#Another if condition, filter for names that don't start with c:
names = ['alice', 'bob', 'carol']
print([name.upper() for name in names if name[0] != 'c'])

#Can do it on strings
print([ch + '!' for ch in "hello"])

#Adding else statement
print([name.upper() if name[0] != 'c' else name for name in names])

#Three ways to go through lists.
#First: Loop variable
stuff = ['foo', 'bar', 'baz']
for word in stuff:
    print(word)

#Second: With index
for i in range(len(stuff)):
    print(i, stuff[i])

#Third: Enumerate
for i, the_thing in enumerate(stuff):
    print(i, the_thing)

#Enumerate in list comprehension
print([t for t in enumerate(stuff)])

#Reversing a list by creating a new list
numerals = [10, 12, 5, 18, 3]
new_numbers = []
for i in range(len(numerals) - 1, -1, -1): #Range: Last digit to first digit, step -1
    new_numbers.append(numerals[i])
print(new_numbers, numerals)

#Reversing a list by changing the original list
print('before', numerals)
for i in range(len(numerals) // 2): #Left of the midpoint
    j = len(numerals) - (i + 1) 
    numerals[i], numerals[j] = numbers[j], numerals[i] #Tuples. Switch
print('after', numerals)

#Adding or removing words during loops can get tricky, loop gets cut off prematurely
random_words = ['foo', 'foo', 'bar', 'baz', 'foo']
for i, word in enumerate(random_words):
    print(i, word)
    if word == 'foo':
        random_words.remove(word)
print(random_words)

#Aliases. Both things map to the same object, so if you change the second, first one changes too
x = [1,2,3]
y = x
y.append(4)
print(x)

#Output is the global variable, which is unchanged.
#Function looked locally first, found local variable, changed that
#Print command is outside the function, so it prints the global value, not local
instruments = []
def add_cow_bell():
    instruments = ['kazoo', 'theremin']
    instruments.append("cow bell")
add_cow_bell()
print(instruments)

#Sum:
digits = [1.5, 2, 4.5]
print(sum(digits))

#Can use max and min on a list, or on a collection of values
print(max(digits)) #Name of list
print(max([4,7,1,9])) #List itself
print(max(4,7,1,9)) #Collection of values

#Using a key. Output is -100
w = [-100, 5, 2]
print(max(w, key=abs)) #Abs here is a built-in function for absolute value

#Without the key, output is 5
w = [-100, 5, 2]
print(max(w))

#The key can be a custom function
def convert2to1000(x):
    return 1000 if x == 2 else x #Converts 2 to 1000
print(max(w, key=convert2to1000)) #Output is 2, because the function converts it to 1000

#Another custom key:
def f(x):
    return 1 / x;
print(max(5, 10, 2, 1, key=f)) #Output is 1, because 1/1 is 1, greater than all the other fractions.

#Sort reorders in place, doesn't give back a value:
w = [-100, 5, 2]
result = w.sort()
print(result) #None
print(w) #Prints sorted list
"""

#Sorted is a built-in function that returns the sorted version of the list
p = [-100, 7, 2, 1, 5]
result = sorted(p)
print(result) 

#Sorted can have a key too
abs_result = sorted(p, key = abs)
print(abs_result)






