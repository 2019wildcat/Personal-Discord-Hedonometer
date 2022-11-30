import csv
import math
import os

dictformat = {}
rootdir = '/Users/elliottchalcraft/Documents/1_Schooling/CMST210 Project/messages'

#reads the discord csv and writes a dictionary with dates as keys and words as values
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == 'messages.csv':
            with open(os.path.join(subdir, file), 'r') as file:
                csvreader = csv.reader(file)
                date_last = 0
                for _,dateLong,message,_ in csvreader:
                    date = dateLong[0:10:1]
                    message = message.split()
                    if date_last == date:
                        for x in message:
                            dictformat[date].append(x)
                    else:
                        dictformat[date] = [x for x in message]
                        date_last = date
                dictformat.pop('Timestamp')

# print(dictformat)
# print()


#reads the Hedonometer word list and writes and dictionary with words as keys and happiness scores as values

wordList = {}

with open("Hedonometer.csv","r") as file:
    csvreader = csv.reader(file)
    for _,_,word,happyScore,_ in csvreader:
        try:
            wordList[word] = float(happyScore)
        except:
            wordList[word] = happyScore
    wordList.pop('Word in English')

    
#compares the list of words from the discord csv to the list of words with happiness scores and removes words that don't have a score
#wordList[word] is the happiness score for that word
happyDict = {}

dictKeys = list(dictformat.keys())

for date in dictKeys:
    dateLast = 0
    for word in dictformat[date]:
        try:
            if dateLast == date:
#                 print(wordList[word])
                happyDict[date].append(wordList[word])
            else:
#                 print()
#                 print(wordList[word])
                happyDict[date] = [wordList[word]]
                dateLast = date
        except:
            dictformat[date].remove(word)
            

for date in happyDict:
    happyDict[date] = sum(happyDict[date])/len(happyDict[date])

#print(happyDict)


%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

dates = list(happyDict.keys())
dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
#print(dates)
x = range(1,len(dates)+1)
y = [happyDict[date] for date in dates]

plt.figure(figsize=(200,10))
plt.xticks(x,dates,rotation=90)
plt.scatter(x, y,alpha=0.5)
plt.show()