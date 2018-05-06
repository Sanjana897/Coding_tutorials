#Class1

print('hello world')
#print('Hola'  won't print because syntax error. Bracket hasn't been closed. 
#print("Howdy" + 2) will start printing then run time error because you can't add a string and integer.
#prin('hello world) won't print either because of print hasn't been spelled correctly

help(print) #gives documentation on the print function

print('Hi','there', 5) #Function takes multiple arguments, separated by commas or plus signs. Strings in quotes, integers as is. 

print("Don't") #To print single quotation, put it in double quotes and vice versa.
#print('Don't') won't work. Need to do double quotes on the outside and then the single quote inside will be treated as part of the string.

print('"Hi"') #To print double quotes, put them in single quotes
#print(""HI"") won't work. Has to be single quotes outside and double quotes inside.

#print('Hi','there', you) will not work because you is neither a string, nor an integer, nor a variable.

print("""Hi""") #Triple double quotes

print("""Hi
I
Am
Sanjana""") #They can be used for multi-line strings

print("""Hi
I'm Sanjana""") #They can have single quotes inside them

#print(""""Hi"""") won't work because has to be exactly three. The fourth one doesn't get recognized as part of the string. Have to write it as print('"Hi"').
#print("""She said "Hi""""") doesn't work either.

"""This is a comment, because it is a benign piece of text, not being operated on in any way. Triple double quotes can also be used as comments."""

print('I\'m Sanjana') #The backslash tells the program that the next character is a string, not an operator, so to ignore it. Can backslash a backslash, if you actually want one in your code.

#print('I\\'m Sanjana') is a syntax error, because now the backslash has been backslashed, meaning it is no longer being treated as a special character, and therefore is not being used as an escape route for the single quote.

print('print this\non a new line') #\n can be used to send text to a new line

#Class exercise, print these lyrics in three different ways:

print("""On a tropical island,
Underneath a molten lava moon.
Hangin' with the hula dancers,
Askin questions cause' they got all the answers.
""")

print('On a tropical island,\nUnderneath a molten lava moon.\nHangin\' with the hula dancers,\nAskin questions cause\' they got all the answers.')

print("On a tropical island,\nUnderneath a molten lava moon.\nHangin' with the hula dancers,\nAskin questions cause' they got all the answers.")

print(5555**5.0) #Python displays large numbers in exponential form

print(type("hello")) #Type tells you the type of value: integer, float or string. Have to print if you want it displayed

print(type(1)) #Integer
print(type(1.0)) #Float
print(type("1")) #Trick question! String
print(type("""1""")) #String again
print(type(1.111)) #Float
print(type('1.111')) #String

print(((9/5)*37)+32) #PEMDAS

print("hey"*3) #Can multiply string with integer. Prints it that many times.

#print("hey"*"hello") won't work because you can multiply two integers, one string and one integer, but not two strings.

print(str(3)+" blind mice") #Converts the integer 3 to a string

exclaim = "!!!" #Variable
print(exclaim)

length = 25
width = 8
area = length*width
print(area) #Get python to do your math. Variables.

name = input("What's your name?") #Input. Has to be stored in a variable or used immediately otherwise computer doesn't hold on to it
print("Hi " + name) 

decibel = input('how loudly?')
number = int(decibel) #Input default is a string. Have to convert to integer
print('hello' + '!'*number)

decibel1 = int(input('how loudly?'))
print('hello' + '!'*decibel1)

decibel2 = input('how loudly?')
print('hello' + '!'*int(decibel2))

#Exercises from Chapter 1:
print(5-2) #Testing out how Python responds to math symbols. All these three work normally
print(5--2)
print(5++2)
#print(5+02) This doesn't work. Leading zeroes are not okay

print((42*60)+42, 'seconds')
print(10/1.61, 'miles')
