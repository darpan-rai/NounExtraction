from textblob import TextBlob
import collections
import sys
import csv
from importlib import reload
from nltk.stem import WordNetLemmatizer
import docx2txt
import regex

reload(sys)
sys.stdout.encoding


def noun_extraction():

    text = TextBlob(lines)
    nouns = text.noun_phrases

    list = []
    for item in nouns:
        w = WordNetLemmatizer().lemmatize(item)
        list.append(w)

    # remove duplicate nouns from list while removing entries with numbers

    list2 = []
    for n in list:
        match = regex.search(r'\d', n)
        if not match:
            list2.append(n)
            counter = collections.Counter(list2)

    # counts to display number of duplicate nouns
    print('initial count:', len(list), 'final count:', len(list2))
    print(list2)

    # writing nouns and frequency into csv file
    noun_log = open('Nouns.csv', 'w')
    fieldnames = ["Nouns","Frequency"]
    csv.DictWriter(noun_log, fieldnames).writeheader()

    for key in counter.keys():
            nouns = key
            frequency = str(counter[key])

            row = nouns + "," + frequency + "\n"
            noun_log.write(row)


Filename = input('Enter File Path:\n')

# If file is in docx format, it is converted to txt before being processed for noun extraction

if Filename.endswith('.docx'):
    lines = docx2txt.process(Filename)

    noun_extraction()

else:

    File = open(Filename)
    lines = File.read()

    noun_extraction()

