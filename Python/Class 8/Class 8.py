#Class 8
"""
#Try and except
#Try doing this, if it works great, ignore except code
#If there's an error, do this

#This works
a = [1, 2, 3]
try:
	print(a[0])
except:
	print("sorry, try another!")

#This doesn't	
a = [1, 2, 3]
try:
	print(a[100])
except:
	print("sorry, try another!")

#Program to convert inches to feet
#If it doesn't work, for whatever reason, give a message
inches = input("inches\n>")
try:
    print(float(inches)/12)
except:
    print("can't do that")

#Split a pizza among a given number of people
#Customize the message based on the type of error
#If user says 0 people, can't divide by 0
#If user puts alphabetical characters, can't divide those
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except ZeroDivisionError:
    print("More for me!")
except ValueError:
    print("That's not a number!")

#Three card monte
#You have a list of three cups, two empty, one with a coin
#Shuffle them randomly using random.shuffle
#Ask user to pick a cup: 0, 1 or 2
#If their cup has the coin they win otherwise they lose
#If they enter something that's not a number, say not a number, you lose
#If they enter a number apart from 0, 1 or 2, say that cup doesn't exist
#Apart from all the known errors, can also say except Exception
#In case something else goes wrong
import random
cups = ['o', 'o', '.']
random.shuffle(cups)

try:
    n = int(input("Pick a cup: 0, 1 or 2\n"))
    if cups[n-1] == '.':
        print("You win!")
    else:
        print("You lose!")
except ValueError:
    print("Not a number\nYou lose")
except IndexError:
    print("That cup doesn't exist\nYou lose")
except Exception:
    print("You lose")

#Tuples: Comma separated values
dogs = "chihuahua", "pug", "chug"
print(dogs)

#String formatting uses tuples
"I've %s this %s before!" % ("seen", "this")

#So does multiple assignment
a, b, c = 1, 2, 3

#This is not a tuple, it's two values in a function call
print(1, 2)

#If using tuple in a function call, need parentheses to denote it
print((1, 2))

#Some basic operations
d = (1,2,3)
print(d + (4, 5, 6)) #Prints (1, 2, 3, 4, 5, 6) but original stays the same
print(d[0]) #Index
print(d[:2]) #Slicing a tuple returns a tuple
print(len(d)) #Length
print(5 in d) #False
print(d*2) #Multiplication

#Can multiply lists too
lst = ["hello"]
print(lst*2)

#Tuple with one element
animal = 'dog',

#Tuple with two elements, one empty
pet = 'dog', ''

#Tuple assignment
#Need to have equal number of values on both sides
#e becomes dog, f becomes ''
e, f = pet

#Tuple assignment
first_name, last_name = ("Hiro", "Protagonist")

#Can iterate over tuples
for value in (1, 2, 3):
    print(value)

#Unpacking tuples
values = (1, 2, 3)
a, b, c = values
print(a)
print(b)

#Can change assignment
c, a, b = values
print(a)
print(b)

#Tuples within lists are retrieved as single objects
#This list has two objects
characters = [("Hiro", "Protagonist"), ("Yours", "Truly")]
for character in characters:
    print(character)

#Can unpack tuples in loops
characters = (("Hiro", "Protagonist"), ("Yours", "Truly"))
for first, last in characters:
    print("first name is " + first)
    print("last name is " + last)

#Can use operators
pairs_of_numbers = [(1, 2), (2, 3)]
for a, b in pairs_of_numbers:
    print(a + b)

#Can use index to loop
points = [(3, 4), (10, 20), (100, 200)]
for p in points:
    print(p[0])

#Functions can return tuples
#Save those values in variables
#Use them in other places
def calculate_3d_point():
    result = (2, 4, 0)
    return result

x, y, z = calculate_3d_point()
print("the z coordinate is %s" % (z))
print("the x coordinate is %s" % (2))

#Using enumerate with tuples
fauna = ['cat', 'owl', 'bat']
enumerate(fauna) #This doesn't give back elements
list(enumerate(fauna)) #This gives back a list, with index and value
for i, value in enumerate(fauna): #This prints them out on each line
    print(i, value)

#Random choice and random shuffle
import random
print(random.choice(fauna)) #Will randomly choose one from the list
print(random.shuffle(fauna)) #Will shuffle them around within the list
"""

#Dictionary syntax
#first_name and fav_candy are keys
#joe and cleo's are values
d = {"first_name":"joe", "fav_candy":"cleo's"}

#Key can be string or integer
#Value can be string, integer, list, float, tuple, dictionary
{28:"foo", 6:"bar", "entirely different":["baz"]}
d2 = {100:[1, 2, 3], "another string": {}}

#Empty dictionary
{}

#Retrieve values from a dictionary using the keys, like a list index
print(d["first_name"])
print(d["fav_candy"])

#If key doesn't exist you get an error
#print(d["height"])

#get method
#Takes two arguments:
#The key of the element you want to retrieve
#An optional default value in case that key doesn't exist yet
#This gives back None
print(d.get("height", None))

#Can assign get value to a variable
result = d.get('first_name')
print(result)

#If a key doesn't exist, can create a new one through assignment
d["last_name"] = "versoza"
print(d)

#If a key exists, can reassign value
#Can’t assign multiple things to the same key. It overwrites previous
d["last_name"] = "v"
print(d)

#Reassigning key to different value
d["last_name"] = ('v', 'versoza', 'quincy')
print(d)

#Can iterate over dictionaries using loops
#But only get back the keys, not the values
for i in d:
  print(i)

#Items: Dictionary view
#Iterable
#Gives back key and value, in tuples
items = d.items()
for t in items:
    print(t)

#Unpacking the tuples in items
for k, v in d.items():
  print(k, v)

#Keys are another dictionary view
#Also iterable
#Give back only keys
keys = d.keys()
for t in keys:
    print(t)

#Values are another dictionary view
#Also iterable
#Give back only values
values = d.values()
for t in values:
    print(t)

#Can also get dictionary views this way
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
print(vehicle.keys())
print(vehicle.values())

#Dictionaries are unordered. If you iterate over them, will do in any order
#Although seems to be printing in order for me
numbers = {"one":"foo", "two":"bar", 3:"baz"}
for k, v in numbers.items():
  print(k, v)

#len() gives back the number of key value pairs
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
print(len(pizza))

#in checks whether a key is in the dictionary or not, returns True or False
result = 'crust' in pizza
print(result)
print('cheese' in pizza)

#pop removes and returns the value at the key specified
vehicle.pop('can fly')
print(vehicle)

#Since it returns a value, can assign that to a variable 
result1 = vehicle.pop('wheels')
print(result1)

#popitem removes and returns an arbitrary key value pair
#With pop item, returns both the key and the value
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.popitem()
print(result1)
print(vehicle)

#Update adds key value pairs from another dictionary
#to the dictionary the update is called on
#If the key already exists in the dictionary, reassigns the value
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
another_vehicle = {'can float':True, 'name':'boat'}
vehicle.update(another_vehicle)
print(vehicle)

#Can change values within the dictionary based on existing values 
f = {'fgm':1, 'fga':2}
f['fga'] = f['fga'] + 1

#But can't do that if the key doesn't exist yet, error
"""
d = {'fgm':1 }
d['fga'] = d['fga'] + 1
"""

#Roll two thee sided dice simultaneously 1000 times
#Add up the results
#Count the frequency of the results… 2 through 6
#Long way to do it
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
    roll = random.randint(1,3) + random.randint(1,3)
    if roll == 2:
        twos += 1
    if roll == 3:
        threes += 1
    if roll == 4:
        fours += 1
    if roll == 5:
        fives += 1
    if roll == 6:
        sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 

#Shorter way to do it using dictionary
#Line 5 of this code:
#1) Assigns the key if it doesn't exist, sets default value to 0, and adds 1
#2) If it does exist, pulls current value, and adds 1
import random
freq_dice_rolls = {}
for i in range(1000):
    roll = random.randint(1,3) + random.randint(1,3)
    freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
print(freq_dice_rolls)




