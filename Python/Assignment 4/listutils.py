"""
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/05/2017
Assignment instructions: https://foureyes.github.io/csci-ga.1120-fall2017-001/assignments/hw04.html
listutils.py
"""
duplicates = []

def finding_duplicates(a_list):
    for element in a_list:
        if a_list.count(element) > 1 and element not in duplicates:
            duplicates.append(element)
    return duplicates   



def has_duplicates(lst):
    finding_duplicates(lst)
    if duplicates == []:
        return False
    else:
        return True



def join_elements(glue, the_list):
    final_string = ""
    list_total = len(the_list)
    for i in the_list:
        if the_list.index(i) != (list_total - 1):
            final_string = final_string + str(i) + glue
        elif the_list.index(i) == (list_total - 1):
            final_string = final_string + str(i)
    return(final_string)



def random_choose(any_list):
    import random
    random_value = random.randint(0, (len(any_list)-1))
    chosen_value = any_list[random_value]
    return chosen_value



def random_fill(min_val, max_val, list_length):
    new_list = []
    import random
    for i in range(0, list_length):
        i = random.randint(min_val, max_val)
        new_list.append(i)
    return new_list
    


def stringify_elements(another_list):
    stringified_list = []
    for i in another_list:
        stringified_list.append(str(i))
    return stringified_list
    

















