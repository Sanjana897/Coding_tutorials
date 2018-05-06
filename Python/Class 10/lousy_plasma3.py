file_object = open('bad_blood.txt', 'r')
phrase = file_object.read()

def create_thesaurus(filename):
    fread = open(filename, 'r')
    thesaurus = {}
    for line in fread:
        line = line.strip() #Gives back a new string without the \n at the end
        line_parts = line.split(',')
        key = line_parts[0]
        value = line_parts[1:]
        thesaurus[key] = value
    return thesaurus

def removing_punctuation(phrase):
    new_string = ""
    for character in phrase:
        if character.isalpha() == False and character.isnumeric() == False and character.isspace() == False:
            continue
        else:
            new_string += character
    return new_string

def substituting_words(phrase, filename):
    import random
    thesaurus = create_thesaurus(filename)
    phrase_minus_punctuation = removing_punctuation(phrase)
    word_list = phrase_minus_punctuation.split(' ')
    new_phrase = []
    for word in word_list:
        key = word.lower()
        if key in thesaurus:
            list_of_synonyms = thesaurus[key]
            random_word = random.choice(list_of_synonyms)
            new_phrase.append(random_word.upper())
        else:
            new_phrase.append(word)
    new_string = ' '.join(new_phrase)
    return new_string
    
        
print(substituting_words(phrase,'thesaurus.txt'))
