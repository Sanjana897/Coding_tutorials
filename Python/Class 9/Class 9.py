#Class 9

nums = [5, 1, 2, 4, 3]
#Can use sort, but it changes the original
nums.sort()
print(nums)

#Can make a copy and sort it
copy = nums [:]
copy.sort()
print(copy)

#Note: Can't make a copy by saying copy = nums
#Both will refer to the same location

#Easier is sorted
#Creates a new list that's sorted
sorted_copy = sorted(nums)
print(sorted_copy)

#To sort in reverse order
sorted_copy = sorted(nums, reverse = True)
print(sorted_copy)

#To sort by dictionary keys
d = {1: 'e', 4: 'r', 3: 'h'}
sorted_list = sorted(d)
print(sorted_list)

#To sort by dictionary value, instead of keys, in reverse
sorted_list = sorted(d, key = d.get, reverse = True)
print(sorted_list)

#To use the sorted list to print the key and value from the dictionary
for k in sorted_list:
    print(k, d[k])

#Random sample function
#Picks sample from population
#random.sample(population, sample size)
import random
print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
