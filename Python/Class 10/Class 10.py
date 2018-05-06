#Class 10

#To open a file in the folder above
file = open("../hi.txt", "w")

#To import only one function from a module, instead of the whole module
from random import randint

from collections import namedtuple

#Defining the namedtuple
#namedtuple returns a new type, like tuple, integer, string, etc
#The type's name is the argument that's passed in, 'Point'
Point = namedtuple('Point', ['x', 'y'])

#Point is a new type of its own, like tuple, integer, string, etc
print(type(Point))

#Once it's defined, two ways to create namedtuples
#The variable name, Point, is bound to the new type that we create…
    #so we can use it to create Point objects
    #(just like we can use list to create lists or str to create strings)
p = Point(x = 0, y = 0)
q = Point(14, 16)

#A point in Point, is recognized as a Point object
print(type(p))

#Accessing items
print(q.x)
print(p[0])

#Unpacking
a, b = q

#Tuples are immutable
#q[0] = 100 will give an error

#Creating a custom error
class CutenessError(Exception):
    pass

#We're creating a new type/class, a Cat!
class Cat:
    #The parameters of the class go here
    def __init__(self, name, cuteness_factor):
        self.name = name
        self.cuteness_factor = cuteness_factor
    #Methods/actions go here:
    #First argument should be self if you want to be able to call it on an instance
    def meow(self, how_loudly):
        print("{} meows{}".format(self.name, how_loudly * '!'))

    #Getters: Methods that get an object's data
    def get_name(self):
        return self.name

    def get_cuteness_factor(self):
        return self.cuteness_factor

    def set_cuteness_factor(self, n):
        #Setters: Validating the data entered:
        if cuteness_factor > 10:
            raise CutenessError("{} is too cute".format(cuteness_factor))
        else:
            self.cuteness_factor = cuteness_factor

    #Override default string representation by creating special method called __str__
    #The value that __str__ returns will be used as the string representation
    #of objects created from your class
    def __str__(self):
        return "the cat named {}".format(self.name)
    

#Creating a new cat named Paw Newman, with cuteness factor, 10
#Number of arguments you pass in match constructor, minus one. The self. 
c = Cat('Paw Newman', 10)

#If the number of arguments don't match, there's an error
#c = Cat('Bill Furry')

#c is an object of type Cat
print(type(c))

#Accessing an object's data directly
print(c.name)
print(c.cuteness_factor)

#Objects are mutable, can reassign
c.cuteness_factor = 2
print(c.cuteness_factor)

#If you try to assign outside parameters, the setter validation will raise an error
#c.cuteness_factor = 2000

#Calling a method on an object
print(c.meow(5))

#Accessing an object's name via getter
print(c.get_name)

#Default string representation is class followed by id
#This prints out the overriden version
print(c)

#Higher order functions, where one is passed in as an argument to the other
def foo(s):
    print(s + '!')

def call_twice(f): 
    f('hello')
    f('hello')

call_twice(foo)


#Function that returns another function
def make_adder(base):

    def new_func(n):
        return base + n
    
    return new_func

addFive = make_adder(5)
addThree = make_adder(3)

print(addFive(1))
print(addThree(1))
