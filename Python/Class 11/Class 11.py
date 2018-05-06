#Class 11

class Dog:
    #Self will be the new instance created when method is called
    #From here, we can augment self by adding properties, values
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.toys = []

    #If you want to reference a property from within your class
    #method, always prefix with self... that will refer to the current instance
    def __str__(self):
        toys_string = ', '.join(self.toys)
        return "A dog named " + self.name + " that has " + toys_string

    def make_noise(self):
        return self.sound.upper()

d1 = Dog('Bark Twain', 'woof')
print(d1.name)
d1.toys.extend(['chew toy', 'pig\'s ear'])
print(d1)
print(d1.make_noise())
d2 = Dog('Jane Clawsten', 'arf')
print(d2.name)
print(d2)
print(d2.make_noise())


class NewPerson:
    
    """Represents the identity of new people"""
    
    def __init__(self, title, first_name, last_name):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return self.title + self.last_name
    def full_name(self):
        return self.first_name + " " + self.last_name
    def say_greeting(self, greeting):
        return greeting + ", my name is " + self.first_name 


p = NewPerson('Ms.', 'Sanjana', 'Gupta')
print(p)
print(p.full_name())
print(p.say_greeting('hello'))


#Declare a static variable within a class:
class Example:
    some_var = 'I am static'

#Access a static variable without instance (use class name):
print(Example.some_var) # I am static

#Access a static variable with instance:
obj = Example()
print(obj.some_var) # I am static

class Example:
    #Prefix it with @staticmethod and don't use the self parameter
    @staticmethod
    def say_hello():
        return 'hello'

#Accessing a static method without an instance (use class name)
#(no need to add self as parameter)
print(Example.say_hello())  # hello

#Accessing a static method with an instance
obj = Example()
print(obj.say_hello()) # hello

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    #Static method to reduce a fraction by finding the greatest common factor:
    @staticmethod 
    def gcf(a, b):
        #Go through every possible factor
        #Check if it divides evenly into both
        #Return the largest one
        cur_gcf = 1
        for factor in range(1, a + 1):
            if a % factor == 0 and b % factor == 0:
                cur_gcf = factor
        return cur_gcf

    #Regular method, must be called with an instance
    def reduce(self):
        #Note how gcf is called / used (no instance needed)!
        gcf = Fraction.gcf(self.n, self.d)
        #Function returns a new instance of the class
        return Fraction(self.n // gcf, self.d // gcf)

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __repr__(self):
        #We can call methods that already defined
        return self.__str__()    

amt_of_pie = Fraction(1, 2)
print(amt_of_pie) # prints out 1/2

a = Fraction(1, 2)
b = Fraction(1, 3)
print(fractions)
print(a + b)
print(a == b)

