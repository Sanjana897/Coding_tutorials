"""
mad_libs_lyrics.py
=====
* find lyrics to one of your favorite songs - about 4 or 5 lines worth of 
  lyrics
* print out each line so that it's outputted to the shell/console
* however, in place of 4 words in your lyrics, use variable names instead
  (see the slides on string concatenation and variables) 
* these words must not be consecutive words (for example, if your lyrics
  were "happy birthday to you", if you choose "happy" as a word to substitute
  with a variable, your next variable cannot be "birthday"
* set your variables equal to strings of your choosing at the top of the file
* name the variables after the part of speech of the word they are replacing, 
  followed by a number:

  verb1 = 'strum'
  adjective1 = 'tiny'
  adjective2 = 'magical'
  noun1 = 'ukulele'
"""

"""
Lyrics:
In the jungle, the mighty jungle
The lion sleeps tonight
Near the village, the peaceful village
The lion sleeps tonight
"""

preposition1 = 'In'
adjective1 = 'mighty'
preposition2 = 'Near'
adjective2 = 'peaceful'

print(preposition1, 'the jungle, the ', adjective1, 'jungle\nThe lion sleeps tonight\n'+preposition2, ' the village, the ', adjective2, ' village\nThe lion sleeps tonight')
