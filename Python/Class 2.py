#Class 2

#Print command comes built in with carriage return at the end. Can bypass that with keyword argument, called end. 
print("one", end="*") #Instead of carriage return, end will now be an asterisk
print("two")

#Default separator between print commands is space. Can bypass that with keyword argument, called sep
print("one", "two", sep="*") #Instead of spaces as separaters, it will use asterisks

formatted = format("hello", ">20s") #String to be formatted and formatting instructions, both in quotes. Can be single or double quotes. > means left indent. 20 means total characters of string plus spaces should be 20. And s means string.
print(formatted)
right_indented = format("hello", '<40s') #Right indented. Can use combination of single and double quotes
print(right_indented)

a = 1.3333333
b = format(a, '.3f') #The dot and the f indicate that it's a float. Three means add three decimal places
c = format(a, '>20.2f') #Add padding to it! Note the order of syntax
print(b, c)

a = 200000000
print(format(a, ',d')) #Can use it to put commas in large numbers. The d indicates it's an integer
print(format(a, '>20,d')) #Add padding to it! Note the order of syntax

#print(format(1.2, 's')) Will not work because the type is incompatible with the value.
#Can leave out type if the operation is not related to that

"""
#Formal way to do this:
name = input("name\n")
if name == 'Kermit' or name == 'Gonzo' or name == 'Skeeter':
    print(name + ' is a muppet!')

#Idiomatic way is a list. In Python, can assign a variable to a list. Can use single or double quotes for the list.v
muppets = ['Kermit', 'Gonzo', 'Skeeter']
if name in muppets:
    print(name + ' is a muppet!')
"""

d,e = 3,4 #Assign multiple variables simultaneously. d = 3, e = 4

#Traditional way to swap the values of both variables, introduce a third:
f = d
d = e
e = f
print(d, e)

#Idiomatic way to swap them:
d,e = e, d
print(d, e) #Note swapped back because the program above swapped them


#Receipt problem. We want to generate a receipt that looks like this:

"""
what is the name of the item? python plush toy
how much does it cost? 5
how many were purchased? 2
how much was paid? 12
(80 wide)
====================================================================
python plush toy x 2                                          $10.00
amount paid                                                   $12.00
change given                                                   $2.00
====================================================================
"""

# gather user input
item_name = input('what is the name of the item?')
cost = float(input('how much does it cost?')) 
quantity = int(input('how many were purchased?')) 
paid = float(input('how much was paid?'))

# total width of receipt
receipt_width = 70

# formatting specifiers
money_format = '.2f' # format as 2 decimal places. formatting can be saved in a variable and applied to multiple values
left_format = '<35s' # total width of string is 35 for left hand column
right_format = '>34s' # total width of money (right column). the default sep is space, so the total width is 70, which 35 + 1 + 34, with 1 coming from the space

total = cost * quantity
change = paid - total

# our actual receipt
print(item_name, cost, quantity, paid)
print('=' * receipt_width)

total_formatted = format('$' + format(total, money_format), right_format)
print(format(item_name + ' x ' + str(quantity), left_format), total_formatted)
paid_formatted = format('$' + format(paid, money_format), right_format)
print(format('amount paid', left_format), paid_formatted)
change_formatted = format(format('$' + format(change, money_format), right_format))
print(format('change given', left_format), change_formatted)


#If statements. Boolean values True and False. Note the sentence case. Everything after if and else are indented, except the last line, which is not indented and therefore independent. 
flag = True
print('one')
if flag:
	print('two')
else:
	print('three')
print('four')


answer = input("you have 12 doughnuts, would you like another dozen?\n>")
if answer == 'yes': #Note the colon. Case sensitivity. If user says Yes, it will not accept it. 
	print('you have 24 doughnuts')
else: #Note the colon here too. Cannot have an else statement without an if statement
	print('you have 12 doughnuts')


response = input('what is 2 to the 4th power?\n>')
if response == 2 ** 4:
	print('yup, you got it!')
	print('good job') #Both these two statements are under the same if statement so both get carried out if it's true
else:
	print('close, but no cigar!')
print('done') #It will print this regardless of which one is true, because this is not indented and therefore independent


secret_number = 11
guess = int(input('Try to guess the secret number\n'))
if guess == secret_number:
    print('Yes, you got it!')
else:
    print('The secret number is', secret_number, 'not', guess)

    
#Elifs allow you multiple paths. If multiple conditions are true, only the first is executed
cake_answer = input('do you want some cake?')
if cake_answer == 'yes':
	print('have some cake')
elif cake_answer == 'maybe':
	print('decide!')
elif cake_answer == 'idk':
	print('????')
else:
	print('no cake 4 u')


#Nested if statements:
day = input("What day is it (ex Thursday, Friday, etc.)?\n> ")
time = int(input("What time is it (in 24 hour time)?\n> ")) # not adventure
delicious_time = 16
if day == 'Friday':
	if time >= delicious_time:
		print("Go ahead, you deserve a treat") 
	else:
		print("Just wait %s more hours" % (delicious_time - time)) 
else:
	print("Don't do it!  Just don't.")


#Dune game. Exercise from textbook.
a1 = input("What is the name of the desert planet that's informally called Dune?\n")
correct_responses = 0

if a1 == "Arrakis" or a1 == "arrakis":
        print("That's right")
        correct_responses = correct_responses + 1
else:
        print("No, it's Arrakis")

b1 = input("What valuable resource is only found on Dune?\n")
if b1 == "spice" or b1 == "the spice" or b1 == "the spice melange":
        print("That's right")
        correct_responses = correct_responses + 1

else:
        print("No, it's spice")

print("You got", correct_responses, "correct responses")


