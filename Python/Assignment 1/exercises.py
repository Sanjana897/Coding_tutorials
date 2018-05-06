"""
exercises.py 
=====
* these three exercises are from the end of Chapter 2 in "How to Think Like a 
  Computer Scientist"
  * http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises
  * do problems #1, #2 and #7
"""

"""
How to Think Like a Computer Scientist - Chapter 2 

1. Take the sentence: All work and no play makes Jack a dull boy. Store each 
   word in a separate variable, then print out the sentence on one line using
   print.

(write this out as code outside of and below this comment)
=============================================================================
"""
all1 = 'All'
work = 'work'
plus = 'and'
no = 'no'
play = 'play'
makes = 'makes'
jack1 = 'Jack'
a = 'a'
dull = 'dull'
boy = 'boy'

print(all1, work, plus, no, play, makes, jack1, a, dull, boy)

"""
How to Think Like a Computer Scientist - Chapter 2 

2. Add parentheses to the expression 6 * 1 - 2 to change its value from 4 to 
   -6.

(write this out as code outside of and below this comment)
=============================================================================
"""
print(6*(1-2))


"""
How to Think Like a Computer Scientist - Chapter 2 

7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 
   51 hours. At what time does the alarm go off? (Hint: you could count on 
   your fingers, but this is not what we’re after. If you are tempted to count
   on your fingers, change the 51 to 5100.) 

   * Use an expression consisting of Python values and operators
   * Use a 24 hour clock ... so start off by thinking of 2pm as 14 (no need
     to add am or pm)  
   * Hint: consider using modulo

(write this out as code outside of and below this comment)
=============================================================================
"""
total = 1400+5100
alarm_is_set_for = total - 4800
print(alarm_is_set_for,'hours')


"""
REMEMBER... Run this file; make sure there are no syntax errors
"""
