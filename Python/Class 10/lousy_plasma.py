thesaurus = { 
    "happy":["glad",  "blissful", "ecstatic", "at ease"], 
    "sad":["bleak", "blue", "depressed"] 
}

phrase = input("Give me a phrase\n")

def removing_punctuation(phrase):
    new_string = ""
    for character in phrase:
        if character.isalpha() == False and character.isnumeric() == False and character.isspace() == False:
            continue
        else:
            new_string += character
    return new_string

def substituting_words(phrase, thesaurus):
    import random
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
    
        
print(substituting_words(phrase, thesaurus))
