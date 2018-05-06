"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 07/11/2017
nba_interactive.py
=====
Using the report.csv file generated from nba.py, create an interactive
program that allows a user to enter a player's name, and, in response,
the program will display that player's shooting percentage. The program
will continually ask for a player name. If the user types in q or quit 
in any casing, then the program will stop asking for names.

To write this program:

1. read the file, report.csv
2. as you read in the file, add each player's name to a dictionary as a
   key... and each player's shooting percentage as the value:
   {"Kevin Durant": 0.51, ...}
3. continually ask the user for a player name
4. if they don't enter q, look up that player in the dictionary and print
   out their shooting percentage

Example output
-----
Enter player name
> Kevin Durant
0.51


"""

report = open("report.csv", "r")

#Creating dictionary
players = {}

while True:
    line = report.readline()
    if len(line) == 0:
        break
    removed_line = line.split('\n')
    split_line = removed_line[0].split(', ')
    players[split_line[0]] = split_line[1]



#Asking for user input, generating response

response = " "
while response.lower() != "q" and response.lower() != "quit":
    response = input("Enter player name\n")
    try:
        print(players[response])
    except KeyError:
        if response.lower() != "q" and response.lower() != "quit":
            print("Sorry that player isn't on this list")

"""
#Did this part two ways because the earlier while loop wasn't working
#But managed to fix it
#Leaving this in, as a different way to do it
while True:
    response = input("Enter player name\n")
    if response.lower() == "q" or response.lower() == "quit":
        break
    else:
        try:
            print(players[response])
        except KeyError:
            print("Sorry that player isn't on this list")
"""    

report.close()
    
