from textblob import TextBlob
from textblob import Word
import sys
import csv
from importlib import reload
import nltk


reload(sys)
sys.stdout.encoding

Filename = 'ArunMuthy_CV_June_2018.txt'
File = open(Filename)
lines = File.read()
# text = TextBlob(lines)        '''tried using textblob, however this does
# textDoc = text.lower()           not return correct nouns'''
# nouns = textDoc.noun_phrases

is_noun = lambda pos: pos[:2] == 'NN'

tokenized = nltk.word_tokenize(lines.lower())    #lower case across diagram
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

#singularize nouns
list = []
for words in nouns:

    w = Word(words)
    sing = w.singularize()
    list.append(sing)

print(list)

# remove duplicate nouns from
unique_nouns = []
for n in list:
    if n not in unique_nouns:
        unique_nouns.append(n)

print(unique_nouns)

print('initial count:',len(list),'final count:',len(unique_nouns))



# noun_log = open('Nouns.csv', 'w')
# fieldnames = ["Nouns", "Description"]
# csv.DictWriter(noun_log, fieldnames).writeheader()
# writer = csv.writer(noun_log, 'unix', delimiter=' ')
#
# for x in nouns:
#     writer.writerow([x])



