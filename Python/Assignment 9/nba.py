"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 07/11/2017
nba.py 
=====

You've been hired as the general manager of the Knicks, and it's your job 
to figure out which basketball players you want to trade for.  You only 
want to trade for players that make at least 50% of the shots they've 
tried and have played at least 50 games.  You have a list of all players 
in the league, with their names, number of games played, average number 
of shots attempted (FGA) and average number of shots made (FGM).  Create 
a report for yourself by doing the following...

Download the located at: 

https://foureyes.github.io/csci-ga.1120-fall2017-001/resources/code/class09/stats-clean.txtl

Use File --> save as ... to save in the __same directory__ as your Python 
program.

Write a program that:

* reads in data from a file called stats-clean.txt, which contains a list 
  of players and their statistics 
    * the first line of the file is the header: NAME,POS,TEAM,GP,FGM,FGA
        * HINT: find a way to skip this first line: perhaps exception
          handling, a flag, checking the string for some specific 
          content, etc.
    * each subsequent row contains player stats
    * the stats are separated by commas
    * for example, in the following line: James Harden,SG,HOU,78,7.5,17.1:
        * Name (NAME) -> James Harden
        * Position (POS) -> SG
        * Team (TEAM) -> HOU
        * Games Played (GP) -> 78
        * Average Shots Made Per Game (FGM) -> 7.5
        * Average Shots Attempted Per Game (FGA) -> 17.1
    * HINT: ... split may come in handy here
* calculate a player's shooting percentage by dividing their shots made 
  by their shots attempted (FGM/FGA)
        * HINT: use exception handling to deal with divide by zero 
          errors, or unexpected data from file
* whittle down this list to only players that:
    * made at least 50% of their shots 
    * have played at least 50 games
* write out the names of these players, along with their shooting 
  percentage into a NEW file
    * the file should be called report.csv
    * each name and shooting percentage will be on one line
    * ... with a comma separating the two
    * it should look similar to this (though results may var depending on
      how you round):

Chris Wilcox,0.72
DeAndre Jordan,0.63
Tyson Chandler,0.64
Greg Smith,0.62
Ryan Hollins,0.63
Andre Drummond,0.61
Hasheem Thabeet,0.63
Brandan Wright,0.6
Nick Collison,0.59
Kosta Koufos,0.57
Dwight Howard,0.58
.
.
.
Kevin Durant,0.51
Chris Kaman,0.51
Andrei Kirilenko,0.5
Larry Sanders,0.51
Ronny Turiaf,0.53
Tim Duncan,0.5
Jason Thompson,0.51
Jan Vesely,0.5
Lance Thomas,0.5
David West,0.5
Kevin Garnett,0.5
Marc Gasol,0.5
Andris Biedrins,0.5
"""


stats = open("stats-clean.txt", "r")
lines = stats.readlines()


#Function that gets rid of the new line and commas between values
#Splits the line and returns values in a comma separated list

def generating_comma_separated_list(lines, i):
    removed_new_lines = lines[i].split('\n')
    split_line = removed_new_lines[0].split(',')
    return split_line


#Using the function to split line 1, which are the keys

keys = generating_comma_separated_list(lines, 0)

all_players = []


#Using a for loop to apply the function to all the other lines
#Converting the numeric values to floats
#Adding each value to a dictionary, using the keys from line 1
#Calculating the shooting percentage
#If ZeroDivision error, the value is set at 0
    #since if they've attempted 0, chances are they scored 0
    #(unless they scored by mistake, is that a thing?)
#If Value Error, the value is set at NA
#Each dictionary is added to the list of all players

for i in range(1, len(lines)):
    split_line = generating_comma_separated_list(lines, i)
    player_dictionary = {}
    for j in range(len(split_line)):
        try:
            player_dictionary[keys[j]] = float(split_line[j])
        except:
            player_dictionary[keys[j]] = split_line[j]
    try:
        player_dictionary["SHOOTING PERCENTAGE"] = float(format((player_dictionary["FGM"]/player_dictionary["FGA"]), '.2f'))
    except ZeroDivisionError:
        player_dictionary["SHOOTING PERCENTAGE"] = 0
    except ValueError:
        player_dictionary["SHOOTING PERCENTAGE"] = "NA"
    all_players.append(player_dictionary)


#Looping over the list of all players
#Ignoring the ones where shooting percentage is NA
#Adding the player to a list of desirable players if they meet the conditions

desirable_players = []
for k in all_players:
        if k["SHOOTING PERCENTAGE"] != "NA":
            if k["GP"] >= 50 and k["SHOOTING PERCENTAGE"] >= 0.5:
                desirable_players.append(k)


#Looping over the list of desirable players
#Putting the name and shooting percentage in a string
    #Since the write function takes only strings and not multiple values
#Creating a new file
#Writing the list to it
                
new_file = open("report.csv", "w")
for dictionary in desirable_players:
    string = "{0}, {1}\n".format(dictionary["NAME"], dictionary["SHOOTING PERCENTAGE"])
    new_file.write(string)
    





new_file.close()
stats.close()





