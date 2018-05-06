#Class 4

#Lists can contain strings, integers, floats and other lists: 
stuff = [1, "one", 2, "two", ["numbers", "strings"]]

nothing = [] #Empty list

print(stuff) #Can print list

print(stuff[0]) #Indexing starts at 0 and goes upward

print(stuff[-1]) #Starts indexing backwards, -1 goes to the last value of the list

a = -1
print(stuff[a]) #If the last item is a list, it'll print that list

print(stuff[-2]) #Start going backwards

#print(stuff[13]) If there is no value in that position it will show an error, for example if there aren't that many values in the list

#print(stuff[1.0]) The index has to be an integer, it can’t be a float

print(stuff[-1][0]) #Can index lists within lists. Also lists within lists within lists

string = "string"
print(string[1]) #All of the above applies to strings as well.

a = [3, 4, 5]
a[0] = "surprise"
print(a) #Lists are mutable; can change the values. This will replace 3 with surprise

stuff[4][1] = "characters" #Can change stuff in the list inside the list
print(stuff)

#Lists with for loops. Works like range. 
some_boolean_values = [True, True, False] 
for b in some_boolean_values:
	print(b) 

#Iterating over lists of lists; print out every element in a line of its own in this list of lists:
outer_list = [['foo', 'bar', 'baz'], [1, 2, 3], [0.25, 0.5, 0.75]]
for inner_list in outer_list:
	for element in inner_list:
		print(element)

#Slicing: print out more than one index at a time. 
colors = ["red", "green", "blue", "taupe"]
print(colors[0:2])
print(colors[2:]) #Assumed until end of list
print(colors[:3]) #Assumed from beginning of list
print(colors[0:100]) #Value can be very high, it'll print till the last value of the list, no error

#Equivalancy. Lists have to be same length and same values. 
print([1, 2, 3] == [1, 2, 3]) #True
print(['a', 'b', 'c'] == [1, 2, 3]) #False
print(['a', 'b', 'c'] != [1, 2, 3]) #True

#Comparisons
['a', 'b', 1, 2] > ['b', 'b', 1, 2] #False. b is greater than a
[5, 2] < [5, 2, 1] #True. The third value makes the second list greater
['x', 'y', 'z'] < ['x', 'a', 'z'] #False. y is greater than a

#Addition and multiplication
toppings = ["mushrooms", "peppers", "onions"]
numbers = [2, 3, 5, 7]
print(toppings + numbers) #Prints first list, then the second
print(toppings * 2)
print(numbers * 2) #Output: [2, 3, 5, 7, 2, 3, 5, 7]

#Length of lists
a = ["foo", "bar", "baz"] #3
b = [] #0
c = ["foo", "bar", "baz", [1, 2, 3]] #4

#Checking whether a value exists in a list
print('c' in ['a','b', 'c']) #True
print('c' not in ['a', 'b', 'c']) #False

#Can do it in if else format
breakfast = ["oatmeal", "tofu scramble", "ramen"]
if "ramen" in breakfast:
	print("ramen for breakfast")
else:
	print("wise decision")

#Can delete stuff from a list
vegetables = ["broccoli", "cauliflower", "brownie sundae", "carrot"]
del vegetables[2]
print(vegetables)

#Upper case:
s = "hello"
print(s.upper())

#Sort
numbers = [5, 3, 4]
numbers.sort()
print(numbers)

#Most methods return a value of none:
dogss = ['terrier']
results = dogss.append('poodle')
print(results) # None. Doesn’t assign result to an updated list
print(dogss) # ['terrier', 'poodle'] List got updated

dogs = []
dogs.append('terrier') #Append, add to the list
dogs.append('pug') #Add to the list after terrier
dogs.append(['doge', 'corgie']) #Add list to the end of the other list
print(dogs[2][1]) #Prints element from inner list
print(dogs[-1][-1]) #Same as above
dogs[0] = 'poodle' #Replace terrier with poodle
dogs[2][0] = 'chug' #Replace item inside inner list
print(dogs[0][0]) #Print first character or first word
#dogs[0][0] = 'd' Can't do this. Can change list element, but not string element
dogs.extend(['terrier','st. bernard']) #Adds the elements of this list to the end of that list
cats = ['maine coone', 'russian blue']
dogs.extend(cats) #Can extend by inidividual elements or by entire list
dogs.remove('maine coone') #Removes first occurence of object in list
del dogs[-1] #Deletes by index position, not object
answer = dogs.pop() #Returns value. And deletes last object from list, st. bernard
print(dogs)
print(answer) #Prints result, which is st. bernard
print(dogs.count("terrier")) #Counts how many times terrier appears
print(dogs.count("chug")) #Shows up as 0 because it's in the inner list, which is a whole unit. No error
print(dogs.index("terrier")) #Shows the index of an object
#print(dogs.index("chug")) #Error because object is not in list. It's in the inner list, which is a whole unit

words = ['foo', 'bar', 'baz', 'qux', 'corge']
words.insert(0, 'surprise!') #Unlike the replace option (see above) this inserts it, so all the values get shifted down by 1
result = words.insert(0, 'did not expect that')
print(result) #Will say none. Does not return a value

"""
NOT WORKING
#Capitalise:
new_list = []
for dog in dogs:
    new_list.append(dog.upper())
print(new_list)
print(dogs)
"""

#Filtering lists
filtered_dogs = []
for dog in dogs:
    if dog[0] == 'p':
        filtered_dogs.append(dog)
print(filtered_dogs)

#Creating a function
def greet_more_input(greeting, num):
        s = greeting * num
        return s

#Calling a function
print(greet_more_input("hello", 5))
print(greet_more_input("hi", 12))

#Takes values from the variables, but the name doesn't matter, so swaps them to be in the right position
num = "hi"
greeting = 20
print(greet_more_input(greeting, num)) 

#Super basic function
def greet():
	return 'hello'

print(greet()) #If you don't call it nothing will happen

#Can call one function within another
def say_moo():
	print("moo")

def main(): #Main is used to indicate this is the main part of the code
	say_moo()
	say_moo()
main() #Calls the function

#Another function
def exclaim(word, num):
	punctuation = num * '!'
	s = word + punctuation
	return s #Without this it will print None

print("hello")
print(exclaim("hi", 1))
print("hey there")
print(exclaim("howdy", 10))

#A function can have multiple return statements if used with if else:
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return x * -1

"""
#But if you try to do multiple returns within the function itself, only the first one gets executed then the function ends:
def problem():
return "is this ok?"
return "no it is not"
print(problem())
"""


#Return stops the function so the three won’t get printed, function gets cut off:
def foo():
	print("one")
	print("two")
	return "foo"
	print("three")
foo()

#Function will stop after the first iteration, because of the return statement:
def experiment():
    for i in range(5):
        return i
print(experiment())

#Now s is a variable local to the function. Trying to access it outside the function will give an error.
def greet():
	s = "hello"
	print(s)
print(s) #ERROR


#Within the function, local gets precedence over global. Global remains unaffected:
s = "hello"
def greet():
	s = "something else"
	print(s) #prints something else, the local version
greet()
print(s) #prints hello, the global version

#Exercise from Lists slides
def half_a_list(any_list):
        any_list = any_list[0:((len(any_list))//2)]
        return any_list
print(half_a_list([1,2,3,4]))

#Exercise from List Methods slides
#Make the last element first
def last_to_first(a_list):
        if len(a_list) == 0:
                return a_list
        else:
                a_list.insert(0, a_list[-1])
                a_list.pop()
                return a_list
print(last_to_first([]))


#Think Python, Chapter 10 Exercises:

#Function that takes a list made up of other lists of integers and adds them up
def nested_sum(list_of_lists):
    total = 0
    for lists in list_of_lists:
        total += sum(lists) #Sum, built-in function
    return total

#Function that replaces each integer in a list with the cumulative total thus far
#Returns a new list
def cumulative_total(a_list):
    total = 0
    cumulative_list = []
    for elements in a_list:
        total += elements
        cumulative_list.append(total)
    return cumulative_list

#Function that returns a new list with first and list element from list passed in
#If it has one element returns it as both values, no elements gives an error
def middle(the_list):
    new_list = [the_list[0], the_list[-1]]
    return new_list

#Checks to see whether the list is sorted or not
def is_sorted(any_list):
    sorted_list = sorted(any_list)
    if sorted_list == any_list:
        return True
    else:
        return False
        
