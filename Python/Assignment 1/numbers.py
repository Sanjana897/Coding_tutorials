"""
numbers.py
=====
Write a program that outputs the number in the thousands, hundreds, tens and 
ones places of a number. 

1. Ask the user for a number
2. Calculate the numbers in the thousands, hundreds, tens and ones places
3. Output each place
4. One soution is to use some numeric operators to determine each place 
   (maybe % and // may help)
5. You may have to calculate each place separately
6. Don't worry about input that's not a positive whole number below 10,000

Example Output - Everything after the greater than sign (>) is user input:

Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
"""
number = int(input('Please enter a number\n'))
m = number//1000
print(m, 'thousands')
c = (number-(m*1000))//100
print(c, 'hundreds')
x = (number-(m*1000)-(c*100))//10
print(x, 'tens')
i = (number-(m*1000)-(c*100)-(x*10))
print(i, 'ones')

#Note: Using roman numerals as variables
