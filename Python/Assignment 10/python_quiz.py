"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 11/18/2017
"""
# create an interactive quiz here

import quizzical

#Part 2: Feeling Quizzy 
"""
q = quizzical.MultipleChoiceQuestion('Which one is real?')
q.add_choice('a', 'griffin')
q.add_choice('b', 'narwhale')
q.add_choice('c', 'mermaid')
q.add_choice('d', 'yeti')
q.set_answer('b')

user_response = input(q)

if q.is_correct_answer(user_response) == True:
    print("You're right! The answer is {}. {}".format(user_response, q.choices["answer"]))
else:
    letter = ""
    for i in q.choices:
        if q.choices[i] == q.choices["answer"]:
            letter = i
            break
        else:
            continue
    print("Nope! That's not right... the correct answer is {}. {}".format(letter, q.choices["answer"]))
"""


#Part 3: Comma Down, It's Only a File
"""
list_of_questions = []
questions = open('questions.csv', 'r')
lines = questions.readlines()

def generating_comma_separated_list(lines, i):
    removed_new_lines = lines[i].split('\n')
    split_line = removed_new_lines[0].split(',')
    return split_line

for i in range(1, len(lines)):
    split_line = generating_comma_separated_list(lines, i)
    q = quizzical.MultipleChoiceQuestion(split_line[0])
    all_choices = split_line[2:]
    q.set_choices(all_choices)
    q.set_answer(split_line[1])
    #It works when I print it from here
    print(q)
    list_of_questions.append(q)
    
print(list_of_questions) #When I print the list it prints the name and location
    
"""

#Part 4: The Part Where I Answer Questions

"""
questions = open('my_questions.csv', 'r')
lines = questions.readlines()

def generating_comma_separated_list(lines, i):
    removed_new_lines = lines[i].split('\n')
    split_line = removed_new_lines[0].split(',')
    return split_line

count = 0

for i in range(1, len(lines)):
    split_line = generating_comma_separated_list(lines, i)
    q = quizzical.MultipleChoiceQuestion(split_line[0])
    all_choices = split_line[2:]
    q.set_choices(all_choices)
    q.set_answer(split_line[1])
    
    user_response = input(q)
    if q.is_correct_answer(user_response) == True:
        print("Right!\n")
        count +=1
        
    else:
        letter = ""
        for i in q.choices:
            if q.choices[i] == q.choices["answer"]:
                letter = i
                print("Wrong! The correct answer is {}. {}\n".format(letter, q.choices["answer"]))
                break
            else:
                continue
                
print("You got {}/{} correct.".format(count, len(lines)-1))
"""

