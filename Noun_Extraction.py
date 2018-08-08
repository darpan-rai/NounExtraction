from textblob import TextBlob
from textblob import Word
import sys
import csv
from importlib import reload
from nltk.stem import WordNetLemmatizer
import docx2txt
import nltk
import re
import regex
reload(sys)
sys.stdout.encoding


def noun_extraction():

    text = TextBlob(lines)       # tried using textblob, however this does
    nouns = text.noun_phrases                 #not return correct nouns

    # is_noun = lambda pos: pos[:2] == 'NN'
    #
    # tokenized = nltk.word_tokenize(lines.lower())  # lower case across diagram
    # nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]



    list = []
    for item in nouns:
        w = WordNetLemmatizer().lemmatize(item)
        list.append(w)

    text2 = ' '.join(list)
    # creating dictionary to calculate frequency using findall

    frequency = {}
    sequence = re.findall(r'\b[a-z]{2,30}\b', text2)

    for word in sequence:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])

        noun_count = open('count.csv', 'w', newline='')
        fieldnames = ["Word", "Count"]
        csv.DictWriter(noun_count, fieldnames).writeheader()
        w = csv.writer(noun_count, 'unix', delimiter=' ')

        w.writerows(frequency.items())

    # remove duplicate nouns from list
    unique_nouns = []
    for n in list:
        if n not in unique_nouns:
          unique_nouns.append(n)

    # counts to display number of duplicate nouns
    print('initial count:', len(list), 'final count:', len(unique_nouns))

    noun_log = open('Nouns.csv', 'w')
    fieldnames = ["Nouns", "Description"]
    csv.DictWriter(noun_log, fieldnames).writeheader()
    writer = csv.writer(noun_log, 'unix', delimiter=' ')

    for index in unique_nouns:
        match = regex.search(r'\d', index)
        if not match:
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
