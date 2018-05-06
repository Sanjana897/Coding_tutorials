#Lottery ticket exercise
#Write a program that creates a lottery ticket. The lottery ticket should:
#Have the words "Lucky Numbers" on the first line
#Contain 5 unique numbers between 1 through 59
#Each number printed from lowest to highest
#Each number printed on its own line
#Be saved to a separate file

import random

lottery_ticket = open("lottery.txt", "w")
lottery_ticket.write("Lucky Numbers\n")

def generate_unique_numbers(how_many):
    list_of_numbers = []
    while len(list_of_numbers) < how_many:
        lucky_number = random.randint(1, 59)
        if lucky_number not in list_of_numbers:
            list_of_numbers.append(lucky_number)
    list_of_numbers.sort()
    return list_of_numbers

list_of_numbers = generate_unique_numbers(5)
for lucky_number in list_of_numbers:
    lottery_ticket.write(str(lucky_number) + '\n')
        
lottery_ticket.close()

#The while loop:
#As long as list doesn't have 5 keep going
#So when it has 4, it doesn't have 5 yet, so goes for one more
#Adds the fifth one, then checks, is it less than 5. No. So it stops.

#Write not like print
#Can't do commas and multiple arguments
#So single argument, and in this case can't concatonate string and int
#So convert the number to string

#-------------------------------------------------

#Reading file with for loop
#Loop variable is each line
#New lines get treated separately, so end up with extra spacing
#Can use strip to get rid of it
reading_file = open("lottery.txt", "r")
for line in reading_file:
    print(line.strip())
reading_file.close()

#Printing out one line with readline()
reading_file = open("lottery.txt", "r")
print(reading_file.readline())
reading_file.close()

#Putting readline() in a for loop to get each line back as a string
#Breaking the loop when the line length is 0, indicating end of text
#Because it always returns a string, even if it's just a new line character ("\n")
#Therefore an empty string means end of file
reading_file = open("lottery.txt", "r")
while True:
	line = reading_file.readline()
	if len(line) == 0:
		break
	print(line)
reading_file.close()

#Using read() to put the whole file into a string
#No extra spaces in this one
reading_file = open("lottery.txt", "r")
contents = reading_file.read()
print(contents)
reading_file.close()

#readlines() makes each line an object in a list
#To get the list view
#Note that new line characters get added to each element of the list
reading_file = open('lottery.txt', 'r')
lines = reading_file.readlines()
print(lines)
reading_file.close()

#To use readlines() and print out each line in the list:
reading_file = open("lottery.txt", "r")
lines = reading_file.readlines()
for line in lines:
	print(line)

#Can have multiple files open simultaneously
#Perform different actions in both
	
file_write = open('doubled.txt', 'w')
file_read = open('lottery.txt', 'r')
for line in file_read:
    file_write.write((line.strip() * 2) + '\n')

file_write.close()
file_read.close()
