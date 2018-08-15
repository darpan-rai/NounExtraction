from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

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
from os import system
from pathlib import Path
import collections
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

reload(sys)
sys.stdout.encoding


root = Tk()
root.geometry("500x120")
root.configure(background="#0033A0")

filepath = ""
destinationFile = ""
counter = {}
sorted_list = []

def setCounter(value):
    global counter
    counter = value


def setSortedList(value):
    global sorted_list
    sorted_list = value


def setGlobalFilePath(name):
    global filepath
    filepath = name
    #print("print from setGlobalFilePath: ",filepath)


def getGlobalFilePath():
    ##print("from getGlobalFilePath",filepath)
    return filepath


def setDestinationFile():
    global destinationFile
    destinationFile = Path(getGlobalFilePath()).parent / "nounsFrequency.csv"
    print("parent: ",destinationFile)
    return destinationFile


#This is where we lauch the file directory browser.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Documents/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )

    textbox.delete('1.0', '2.0')
    textbox.insert('1.0', name)
    setGlobalFilePath(name)

    #Using try in case user types in unknown file or closes without choosing a file.
    #try:
    #    with open(name,'r') as UseFile:
    #        print(UseFile.read())
    #except:
    #    print("No file exists")

#######################################################################################################################
def noun_extraction():
    # If file is in docx format, it is converted to txt before being processed for noun extraction
    if getGlobalFilePath().endswith('.docx'):
        lines = docx2txt.process(getGlobalFilePath())


    else:

        with open(getGlobalFilePath().strip()) as file:
            lines = file.read()

    text = TextBlob(lines)  # tried using textblob, however this does
    nouns = text.noun_phrases  # not return correct nouns

    text = TextBlob(lines)
    nouns = text.noun_phrases

    list = []
    for item in nouns:
        w = WordNetLemmatizer().lemmatize(item)  # takes every word to its base form
        list.append(w)

    # remove duplicate nouns from list while removing entries with numbers

    list2 = []
    for n in list:
        match = regex.search(r'\d', n)  # eliminate 'nouns' containing numbers
        if not match:
            list2.append(n)

    setSortedList(sorted(list2, key=list2.count, reverse=True))  # sort in order of descending frequency
    setCounter(collections.Counter(sorted_list))  # frequency count

    getfrequency()
    plot()

#######################################################################################################################

def getfrequency():
    noun_log = open(setDestinationFile(), 'w')
    fieldnames = ["Nouns","Frequency"]
    csv.DictWriter(noun_log, fieldnames).writeheader()

    for key in counter.keys():
            nouns = key
            frequency = str(counter[key])

            row = nouns + "," + frequency + "\n"
            noun_log.write(row)
#######################################################################################################################

def plot():
    plt.ylabel('Noun')
    plt.xlabel('Frequency')
    plt.xticks(rotation='vertical')
    plt.title('Noun vs Frequency')
    plt.hist(sorted_list,rwidth=0.85,bins=len(counter))
    plt.show()
#######################################################################################################################


Title = root.title("Noun Finder v1.0")

topFrame = Frame(root, bg="#0033A0", height=10)
midFrame = Frame(root, bg="#0033A0")
separatorframe = Frame(root, bg="#0033A0", height=20)
midBottomFrame = Frame(root)
bottomframe = Frame(root, bg="#0033A0", height=30)

topFrame.pack()
midFrame.pack()
separatorframe.pack()
midBottomFrame.pack()
bottomframe.pack(side=BOTTOM)

textbox = Text(midFrame, width=50, height=1)
textbox.insert('1.0', 'Browse')

browseButton = Button(midFrame, text="BROWSE", command=OpenFile, bg="#00B140", fg="white")
goButton = Button(midBottomFrame, text="GO", command=noun_extraction, width=50, bg="#00B140", fg="white")


textbox.pack()
browseButton.pack(side=RIGHT)
goButton.pack()


root.mainloop()