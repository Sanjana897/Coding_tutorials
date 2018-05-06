"""
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 09/18/2017
"""

"""
sticky.py
=====
Create a game of pick-up sticks where the player plays against the computer. 

Pick-up Sticks Rules

* there are some number of sticks on the table
* 2 player alternate turns picking up 1, 2 or 3 sticks
* the player that picks up the last stick loses

In our version of the game...

* the player chooses the minimum and maximum number of sticks available on the
  table (based on those values, some number of sticks will be placed on the 
  table)
* if the minimum and maximum values result in 0 (or less!) possible sticks, 
  end the game immediately (see text in sample runs)
* the player then chooses who should go first, the player or the comuter by 
  typing in p for player or c for computer
* if the player does not enter p or c... ask again until they enter valid
  input!
* after determining who goes first, display the number of sticks on the table
* then... continually do the following until there are no more sticks:
    * if it's the player's turn, ask them how many sticks they want to pick up
        * limit their choice to 1 - 3 sticks... 
        * ask them again if they enter a number that is not within this range
        * hint: there are multiple ways to do this... from using a while loop
          within a while loop, using continue, nested if statements, etc.
    * if it's the computer's turn choose a random value between 1 and 3 for
      the computer to pick up
      * make sure that the value doesn't cause the number of total sticks to be
        negative
      * EXTRA CREDIT (1 point): come up with a better strategy than random so
        that the computer actually wins every now and then (or all the time
        depending on the game's original settings)!
* display who lost the game; again, this is determined by who picked up the 
  last stick(s)
* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

Example runs...

Run 1 (end the game if min and max number of sticks is not valid)
-----
Enter the minimum number of sticks
> 5
Enter the maximum number of sticks
> 3
Um - sry, you can't play a valid game with min 5 sticks and max 3 sticks. I'm leaving!
(╯°□°）╯︵ ┻━┻


Run 2 (continue to ask for who goes first if player does not enter p or c)
-----
Enter the minimum number of sticks
> 5
Enter the maximum number of sticks
> 10
Who goes first (p)layer or (c)omputer?
> me!
I expected (p)layer or (c)omputer
Who goes first (p)layer or (c)omputer?
> compy 3000
I expected (p)layer or (c)omputer
Who goes first (p)layer or (c)omputer?
> p
There are 5 sticks
How many sticks do you want to pick up (1 - 3)?
... (see below for a sample run of an entire game)


Run 3 (an example of a full run where the computer loses)
-----
Enter the minimum number of sticks
> 10
Enter the maximum number of sticks
> 15
Who goes first (p)layer or (c)omputer?
> p
There are 10 sticks
How many sticks do you want to pick up (1 - 3)?
> 1
Player picked up 1 sticks
There are 9 sticks left

Computer picked up 1 sticks
There are 8 sticks left

How many sticks do you want to pick up (1 - 3)?
> 3
Player picked up 3 sticks
There are 5 sticks left

Computer picked up 2 sticks
There are 3 sticks left

How many sticks do you want to pick up (1 - 3)?
> 2
Player picked up 2 sticks
There are 1 sticks left

Computer picked up 1 sticks
There are 0 sticks left

Computer lost because they took the last turn!
"""

#Step 1
minimum = int(input("Enter the minimum number of sticks\n"))
maximum = int(input("Enter the maximum number of sticks\n"))
import random

#Step 2
if minimum > maximum or minimum == maximum or maximum <= 0 or minimum < 0:
    print("Sorry, you can't play a valid game with minimum %i sticks and maximum %i sticks" % (minimum, maximum))

#Steps 3, 4, 5
else:
    num_sticks = random.randint(minimum, maximum)
    first = input("Who goes first (p)layer or (c)omputer?\n")
    while first != "p" and first != "c":
        print("I expected (p)layer or (c)omputer")
        first = input("Who goes first (p)layer or (c)omputer?\n")
    print("There are %s sticks on the table" %(num_sticks))
    
    if first == "p":
        player_response = int(input("How many sticks do you want to pick up (1 - 3)?\n"))
        while player_response > num_sticks:
            print("There aren't enough sticks, pick again")
            player_response = int(input("How many sticks do you want to pick up (1 - 3)?\n"))
        print("Player picked up %i sticks" % (player_response))
        num_sticks -= player_response
        print("There are %i sticks left\n" %(num_sticks))
        if num_sticks == 0:
            print("Player lost because they look the last turn")
                
    while num_sticks > 0:
        computer_reponse = random.randint(1, 3)
        if computer_reponse > num_sticks:
            computer_reponse = random.randint(1, num_sticks)
        print("Computer picked up %i sticks" % (computer_reponse))
        num_sticks -= computer_reponse
        print("There are %i sticks left\n" %(num_sticks))
        if num_sticks == 0:
            print("Computer lost because they look the last turn")
            break

        player_response = int(input("How many sticks do you want to pick up (1 - 3)?\n"))
        while player_response > num_sticks:
            print("There aren't enough sticks, pick again")
            player_response = int(input("How many sticks do you want to pick up (1 - 3)?\n"))
        print("Player picked up %i sticks" % (player_response))
        num_sticks -= player_response
        print("There are %i sticks left\n" %(num_sticks))
        if num_sticks == 0:
            print("Player lost because they look the last turn")
    

        
