"""
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 09/24/2017
"""

"""
counting.py
=====

use *while* loops to do the following:

* print out "while loops"
* use a while loop to count from 2 up-to and including 10 by 2's.
* use another while loop to count down from 5 down to 1


use *for* loops to do the following:

* print out "for loops"
* use a for loop to count from 2 up-to and including 10 by 2's.
* use another for loop to count from 5 down to 1.

* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

example output:

while loops
2
4
6
8
10
5
4
3
2
1
for loops
2
4
6
8
10
5
4
3
2
1
"""

print("while loops")

#While loop, counts from 2 up-to and including 10 by 2's
count = 2
while count < 11:
    print(count)
    count += 2

#While loop, counts down from 5 to 1
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

#For loop, counts from 2 up-to and including 10 by 2's        
print("for loops")
for i in range(2, 11, 2):
    print(i)

#For loop, counts down from 5 to 1
for j in range(5, 0, -1):
    print(j)
