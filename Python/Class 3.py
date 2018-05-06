#Class 3

#print("My name is " + name + ". I have " + str(num) + " " + animal) Instead of string concatonation, use %s string formatting. 

template = "string" #template is the variable, can use any. %s is the placeholder and then whatever is in the bracket %() is what goes inside.  
print("This is a %s" % (template))

print("This is a %s" % ("string")) #Can also do it all in the same line, without variable. Note that if it's a string, has to be in quotes. If variable can be as is.
print("My name is %s and I am %s years old" % ("Sanjana", "25")) #Can do multiple substitutions at the same time, just separate by commas in the bracket.

print("%i is an integer" %(3)) #To do the same with an integer
print("%f is a float" %(5.0)) #To do the same with a float
print("%f is a float" %(5)) #Converts integer to float
print("%i is an integer" %(5.3)) #Converts float to integer

#Ask for input and substitute that value:
name = input("What is your name?")
print("Hello %s" %(name))

#To print 1-5
print(1)
print(2)
print(3)
print(4)
print(5)

#Or can do:
x = 1
delta = 1
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta
print(x)
x = x + delta

while True:
    print("hello") #Will print an endless number of hellos. Because at no point is True being changed to false. So need a condition outside the loop that stops it.

keep_on_going = True
while keep_on_going:
	print("I'm going!") #Same as above

while False:
    print("False") #Won't even print because the condition is false.

while 1 == 'hello':
    print('hello') #Won't print because the condition is false.

keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False #Now condition is changed to False, so it stops itself. Known as sentinel variable.

#counts 1 through 5 by ones
count = 1
while count <= 5:
    print(count)
    count = count + 1 #Known as an accumulator variable

#counts 2 through 8 by 2's
count = 2
while count <= 8:
    print(count)
    count = count + 2

#prints all of the odd numbers from 1-99, skips 13
n = 1
while n <= 99:
    if n != 13:
        print(n)
    n = n + 2

#Keep asking if they want cake till they say yes:
response = input('want some cake?')
while response != 'yes' or response != 'yeah':
    input('want some cake')
#the or is problematic. one holds true. change to and. Problem is the OR, need to change to AND. Because OR is true if either one side is true. So doesn’t stop even if they say yes, because though that one side is now false, the other side is still true.

#So do this instead. When one becomes false the whole thing becomes false and it stops.
response = input('want some cake?')
while response != 'yes' and response != 'yeah':
    input('want some cake')

#These two boolean expressions are not the same:
answer == "yes" or "yea"
answer == "yes" or answer == "yea"
#Each part on either side of the or are treated separately.
#The first one, answer == "yes" is one part that is true or false.
#The other side, "yea" will always prove true. Inherent truthiness.
#And because one side is true, the whole condition will prove true, since it’s OR. 
"" 0 False and [] have an inherest falsiness. Empty quotes or brackets, or 0.
"Anything in here" 1 True and [Anything in here] have an inherent truthiness. Any value, anything in the string.
"False" is also true, just because it's not an empty string.

#Ask for number and keep adding it to the total
total = 0
while True:
    answer = int(input('give me a num!!!'))
    total = total + answer
    print('current total is %s' % (total))

#Ask for numbers and keep totalling. Ask if they want to keep going. When they say no, print the average
print("I'll calculate the average for you!")
print("Current total: 0")
print("Numbers summed: 0")

current_total = 0
numbers_summed = 0
answer = "yes"

while answer == "yes":
    response = int(input("Please enter a number to add\n"))
    current_total = current_total + response
    numbers_summed = numbers_summed + 1
    print("Current total: %s" % current_total)
    print("Numbers summed: %s" % numbers_summed)
    answer = input("Should we continue? yes or no\n")

average = current_total /numbers_summed
print("The average is %s" % average)

#Syntactic sugar. n += 1 is the same as n = n + 1
c = 5
c += 2
print(c) 

#Syntactic sugar. n -= 1 is the same as n = n - 1
m = 5
m -= 2
print(m)

#Syntactic sugar. n *= 2 is the same as n = n * 2 
a = 5
a*= 2
print(a)

#Syntactic sugar. n /= 2 is the same as n = n / 2
b = 10
b /= 2
print(b)

#Also works with strings
s = "h"
s += "e"
s += "y"
print(s)

#Exercise: Ask for a word and how many exclamation points. Print out resulting word and exclamation points.
word = input("Give me a word\n")
num_exclaim = int(input("How many exclamation points?\n"))
word += num_exclaim*"!"
print(word)

#Will print 0-4. i is the loop variable and the range is the iterable object.
#For each element in your sequence, the loop variable is set to that element
#Starting point is assumed to be 0, step is assumed to be 1. End point is 5, and it's exclusive, so 5 is not printed
for i in range(5):
    print(i)

#Iterable object is a list.
names = ['finn', 'jake', 'pb']
for name in names:
    print(name)

#Iterable object is a string
animal = 'narwhal'
for letter in animal:
    print(letter)

#Start and end specified. Step asssumed to be 1. Start is 1, inclusive, so will be printed. End point is 5, and it's exclusive, so 5 is not printed
for i in range(1, 5):
    print(i)

#Step is 2, so prints only 1 and 3
for i in range(1, 5):
    print(i)
for i in range(1, 5, 2):
    print(i)

#With a negative step, you go backwards
for num in range(100, 0, -1):
    print(num)

#Prints nothing because end point has already passed
for num in range(10, 0):
    print(num)

numbers = range(5)
print(numbers) #Shows the range
print(type(numbers)) #Shows what type it is, ie. range
print(list(numbers)) #List function lets you see all the numbers in the range

#Prints 1 Mississippi, 2 Mississippi, 3 Mississippi
for whatevs in range(1, 4):
    print(str(whatevs) + " Mississippi")

#Prints squares of 6, 9 and 12
for num in range(6, 13, 3):
    result = num * num
    print(str(num) + " squared is " + str(result))

#Skips 2 Mississippi. If else nested in for loop
for whatevs in range(1, 4):
    if whatevs == 2:
        print("let's skip this one")
    else:
        print(str(whatevs) + " Mississippi")

#Prints 1-100
for num in range(1,101):
    print(num)

#Count to 100 by twos from 0
for num in range(0,101,2):
    print(num)

#Print 1-100. Multiples of 3 are fizz, multiples of 5 are buzz and multiples of both are fizzbuzz.
#Works except for the fizzbuzz. Because the earlier condition proves true. So just does that. So need to reorder them and put the narrowest condition first.  
for number in range(1, 101):
    if number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    else print(number)

#Corrected:
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)

#Sum the first 1-100 numbers, print out the resulting the sum
sum = 0
for num in range(1,101):
    sum = num + sum
print (sum)

#Roll a die 1000 times; count how many times a one is rolled! Print out the result.
import random
count = 0
ones = 0
while count <= 1000:
    dice = random.randint(1,6)
    count += 1
    if dice == 1:
        ones += 1 
print(ones)

#Ask for a height, make a ladder with that many rungs
height = int(input('How tall do you want this ladder to be?\n'))
for i in range(height):
    print('========\n|      |')

#Can also do it through multiplication:
print(height * '========\n|      |')

#Print out the square root of every multiple of 4 that's less than 65, but greater than 3
import math

for i in range(4, 65):
    if i % 4 == 0:
        print(math.sqrt(i))

#ATM program
#ATM program that displays your current balance, which starts at 5.
#It repeatedly asks for one of three commands: deposit, withdraw or quit
#If the command is withdraw or deposit, the program asks for an amount (that will be added/subtracted)
#If the command is q, the program stops running
#If the command is not recognized, print "huh?"

balance = 5
print("Your current balance is %i" %(balance))
user_response = "d"
while user_response != "Q" and user_response != "q":
    user_response = input("(D/d)eposit, (W/w)ithdraw or (Q/q)uit?\n")
    if user_response == "D" or user_response == "d":
        deposit_amount = int(input("How much would you like to deposit?\n"))
        balance += deposit_amount
        print("Your current balance is %i" % (balance))
    elif user_response == "W" or user_response == "w":
        withdrawal_amount = int(input("How much would you like to withdraw?\n"))
        balance -= withdrawal_amount
        print("Your current balance is %i" % (balance))
    elif user_response == "Q" or user_response == "q":
        print("k thx bye")
    else:
        print("Huh?")
        print("Your current balance is %i" % (balance))

#Textbook exercise, break
#The loop condition is True, which is always true, so the loop runs until it hits the break statement.
#Each time through, it prompts the user with an angle bracket. If the user types done, the break statement exits the loop.
#Otherwise the program echoes whatever the user types and goes back to the top of the loop. 

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')
