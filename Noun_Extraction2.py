from textblob import TextBlob
import collections
import sys
import csv
from importlib import reload
from nltk.stem import WordNetLemmatizer
import docx2txt
import regex
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

reload(sys)
sys.stdout.encoding


def noun_extraction():

    text = TextBlob(lines)
    nouns = text.noun_phrases

    list = []
    for item in nouns:
        w = WordNetLemmatizer().lemmatize(item)                 # takes every word to its base form
        list.append(w)

    # remove duplicate nouns from list while removing entries with numbers

    list2 = []
    for n in list:
        match = regex.search(r'\d', n)                          # eliminate 'nouns' containing numbers
        if not match:
            list2.append(n)

    sorted_list = sorted(list2, key=list2.count, reverse=True)  # sort in order of descending frequency
    counter = collections.Counter(sorted_list)                  # frequency count



    # counts to display number of duplicate nouns
    print('initial count:', len(list), 'final count:', len(list2))

    # writing nouns and frequency into csv file


    noun_log = open('Nouns.csv', 'w')
    fieldnames = ["Nouns","Frequency"]
    csv.DictWriter(noun_log, fieldnames).writeheader()

    for key in counter.keys():
            nouns = key
            frequency = str(counter[key])

            row = nouns + "," + frequency + "\n"
            noun_log.write(row)

    plt.ylabel('Noun')
    plt.xlabel('Frequency')
    plt.xticks(rotation='vertical')
    plt.title('Noun vs Frequency')
    plt.hist(sorted_list,rwidth=0.85,bins=len(counter))
    plt.show()


Filename = input('Enter File Path:\n')

# If file is in docx format, it is converted to txt before being processed for noun extraction

if Filename.endswith('.docx'):
    lines = docx2txt.process(Filename)

    noun_extraction()

else:

    File = open(Filename)
    lines = File.read()

    noun_extraction()

