# from textblob import TextBlob
from textblob import Word
import sys
import csv
from importlib import reload
import nltk
import docx2txt

reload(sys)
sys.stdout.encoding


# text = TextBlob(lines)        '''tried using textblob, however this does
# textDoc = text.lower()           not return correct nouns'''
# nouns = textDoc.noun_phrases
def noun_extraction():
    is_noun = lambda pos: pos[:2] == 'NN'

    tokenized = nltk.word_tokenize(lines.lower())  # lower case across diagram
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    # singularise nouns, pluralizing might add 's' to any plural words.

    list = []
    for words in nouns:
        w = Word(words)
        sing = w.singularize()
        list.append(sing)

    print(list)

    # remove duplicate nouns from document
    unique_nouns = []
    for n in list:
        if n not in unique_nouns:
            unique_nouns.append(n)

    print(unique_nouns)

    # counts to display number of duplicate and plural nouns
    print('initial count:', len(list), 'final count:', len(unique_nouns))

    noun_log = open('Nouns2.csv', 'w')
    fieldnames = ["Nouns", "Description"]
    csv.DictWriter(noun_log, fieldnames).writeheader()
    writer = csv.writer(noun_log, 'unix', delimiter=' ')

    for index in unique_nouns:
        writer.writerow([index])


Filename = input('Enter File Path:\n')

# If file is in docx format, it is converted to txt before being processed for noun extraction

if Filename.endswith('.docx'):
    lines = docx2txt.process(Filename)

    noun_extraction()

else:

    File = open(Filename)
    lines = File.read()

    noun_extraction()

