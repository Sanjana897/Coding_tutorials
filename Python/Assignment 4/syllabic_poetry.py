"""
syllabic_poetry.py
Class: Introduction to Programming
Student name: Sanjana Gupta
Date: 10/05/2017
Assignment instructions: https://foureyes.github.io/csci-ga.1120-fall2017-001/assignments/hw04.html
"""
# add your imports here
import listutils
import random

# this is a partial implementation of generate_word
# it contains a list of lists, with each sub list
# containing words with the same number of syllables
# ...the first sub list contains words with only one
# syllable, the second, two syllables, etc.
def generate_word(syllables_in_word):
    available_words = [
        ['age', 'roof', 'plain', 'slime', 'floor', 'fig', 'rode', 'oomph', 'flab', 'chit', 'creek', "we'll", 'brail', 'bay', 'big', 'salve', 'yaws', 'heal', 'bring', 'stir', 'bah', 'con', 'rone', 'team', 'nought', 'gill', 'rare', 'plains', 'bowls', 'wee', 'queue', 'gun', 'etch', 'set', 'mode', 'miss', 'ate', 'darn', 'rusk', 'mast', 'box', 'their', 'duds', 'depth', 'lien', 'rob', 'deek', 'word', 'quell', 'hark', 'home', 'pledge', 'brown', 'rune', 'pike', 'sprout', 'trace', 'cot', 'nob', 'nonce', 'dear', 'sense', 'sleek', 'poke', 'hut'],
        ['stunner', 'sucrose', 'begone', 'scorecard', 'humble', 'crouton', 'trimming', 'pudding', 'henchman', 'cackle', 'coffee', 'coma', 'aces', 'prudence', 'rematch', 'hipper', 'chopper', 'imprint', 'purple', 'second', 'lowbrow', 'faucet', 'bureau', 'commune', 'endive', 'stakeout', 'sourpuss', 'cave-in', 'shipyard', 'honors', 'kowtow', 'okra', 'haler', 'rattan'],
        ['echoless', 'fluidly', 'catchier', 'cathartic', 'lawnmower', 'physicist', 'huntedly', 'unzipping', 'centigrade', 'cheekily', 'tectonics', 'clearheaded', 'seditious', 'anodized', 'vehicle', 'sprightliest', 'prevention', 'vehement', 'mnemonics', 'steamroller', 'spikiest', 'persuasive', 'randomly', 'forensics', 'uneasy', 'dizziness', 'nonhuman', 'ethanol', 'connection', 'shrewishly', 'fingerprint'],
        ['nongalactic', 'lacerating', 'optometer', 'troglodytic', 'regradated', 'uniformize', 'chlorination', 'retotaling', 'acceptable', 'culmination', 'forbiddingness', 'immoveable', 'disconcerted', 'prosperity', 'vapourizing', 'profitably', 'envelopment', 'unsealable', 'librarian', 'transmissiveness', 'willowpattern', 'nationalise', 'devotedness', 'clangorously', 'likeableness', 'troubleshooting', 'weakheartedly', 'obsoleteness'],
        ['unsublimated', 'hyperanarchy', 'cylindrically', 'irrationally', 'quasipractical', 'sulfurization', 'undermeasuring', 'victoriously', 'disquietingly', 'metaphysical', 'quasihistoric', 'undesirably', 'soporiferous', 'underrespected', 'unsymmetrical', 'reliberating', 'curability', 'nonrevolution', 'nonscientific', 'marbleization', 'wearability', 'supervexation', 'misconjugating', 'inattentiveness', 'unruinable', 'incorporeal', 'stereoscopic', 'overpolicing', 'noncombustible', 'communicable', 'janitorial', 'etymologist', 'unconnectedness', 'personality', 'unmaintainable', 'geodesical', 'sociologist', 'fortitudinous', 'elimination'],
        ['disaffiliated', 'redeemability', 'misauthorization', 'renegotiated', 'zootomically', 'microbacteria', 'malleability', 'intermediaries', 'supportability', 'eliminatory', 'nonhierarchical', 'quasiadvantageous', 'palaeontology', 'typographically', 'radioactively', 'hyperpotassemic', 'collapsibility', 'selfdramatization', 'hallucinatory', 'megalomania', 'communicativeness', 'quasisatirical', 'nontechnological', 'electrosensitive', 'overintensity', 'excommunicating', 'fundamentality', 'photoelectrical', 'visualization', 'incommensurable', 'noncontinuity', 'etymological', 'overemotional'],
        ['electrometallurgist', 'discreditability', 'nonperfectibility', 'etherealization', 'inexhaustibility', 'unautomatically', 'overdeliberated', 'nonuniversality', 'encyclopaedically', 'paradoxicality', 'hieroglyphically', 'hypercivilization', 'biogenetically', 'incompatibility', 'unconstitutionalism', 'unutilitarian', 'overidealizing', 'transcendentalization']
        ]
    if syllables_in_word > 7 or syllables_in_word < 1:
        return None
    else:
        word = listutils.random_choose(available_words[(syllables_in_word)-1])
        return word
    
def generate_line(syllables_in_line):
    current_total_syllables = 0 
    line = ""
    while current_total_syllables < syllables_in_line:
        max_syllables_per_word = 7
        if syllables_in_line - current_total_syllables < 7:
            max_syllables_per_word = syllables_in_line - current_total_syllables
        current_syllables = random.randint(1, max_syllables_per_word)
        line += generate_word(current_syllables) + " "
        current_total_syllables += current_syllables
    return line
    

def generate_lines(all_lines):
    poem = []
    for i in all_lines:
        poem.append(generate_line(i)) 
    return poem


poem_type = input("I would like to write some poetry for you. Would you like a...\n* (h)aiku\n* (t)anka\n* (r)andom 5 line poem, or do you want to\n* (s)pecify lines and syllables for each line?\n")
if poem_type == "h":
    all_lines = [5, 7, 5]
    print("Here is your poem (5-7-5):")
    print(*generate_lines(all_lines), sep = "\n") #Looked up the formatting on Stack Overflow
elif poem_type == "t":
    all_lines = [5, 7, 5, 7, 7]
    print("Here is your poem (5-7-5-7-7):")
    print(*generate_lines(all_lines), sep = "\n")
elif poem_type == "r":
    all_lines = listutils.random_fill(1, 15, 5) 
    random_poem_syllables = listutils.join_elements('-', all_lines) 
    print("Here is your poem (", random_poem_syllables, ")", sep="")
    print(*generate_lines(all_lines), sep = "\n")
elif poem_type == "s":
    all_lines = []
    response = "y"
    count = 1
    while response != "n":
        num_syllables = int(input(("How many syllables for line %i?\n") %(count)))
        all_lines.append(num_syllables)
        response = input("There are currently %i lines. Add another line? (y/n)\n" %(count))
        count += 1
    selected_poem_syllables = listutils.join_elements('-', all_lines) 
    print("Here is your poem (", selected_poem_syllables, ")", sep="")
    print(*generate_lines(all_lines), sep = "\n")
else:
    print("ERROR\nA crash reduces\nYour expensive computer\nTo a simple stone")
