"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 11/18/2017
"""
# Add your MultipleChoiceQuestion class to this file

class InvalidCharacterError(Exception):
    pass

class ChoiceDoesNotExistError(Exception):
    pass

class MultipleChoiceQuestion:
    def __init__(self, question_text):
        self.question_text = question_text
        self.answer = None
        self.choices = {}

    def add_choice(self, letter, text):
        if len(letter) == 1 and letter.isalpha() == True and letter.islower() == True:
            self.choices[letter] = text
        else:
            raise InvalidCharacterError
            print('Error: A choice should have a lowercase letter as its label')
            
    def set_choices(self, all_choices):
        for i in range(len(all_choices)):
            letters = "abcdefghijklmnopqrstuvwxyz"
            self.add_choice(letters[i], all_choices[i])
            
    def set_answer(self, letter):
        try:
            self.choices["answer"] = self.choices[letter]
        except ChoiceDoesNotExistError as e:
            print('Error: None of your choices matches that answer')

    def is_correct_answer(self, letter):
        if self.choices[letter] == self.choices["answer"]:
            return True
        else:
            return False
    def __str__(self):
        string = self.question_text + "\n=====\n"
        sorted_choices = sorted(self.choices)
        for letter in sorted_choices:
            if letter == "answer":
                continue
            else:
                string += "{}. {}\n".format(letter, self.choices[letter])
        return string

q1 = MultipleChoiceQuestion('Which type is immutable?')
q1.add_choice('a', 'list')
q1.add_choice('b', 'tuple')
q1.add_choice('c', 'dict')
q1.set_answer('d')
print(q1)
        
