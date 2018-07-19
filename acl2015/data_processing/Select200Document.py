import os
from random import shuffle

fold = 5
inputFolder = "sample_data/180709_2"
outputFolder = "sample_data/180709_2_100"
inputData = []
inputName = []
outputFiles = []

for filename in os.listdir(inputFolder):
    filename = inputFolder + "/" + filename
    data = []
    with open(filename, "r") as inputFile:
        for line in inputFile:
            data.append(line)
    print filename.split("/")[-1].split(".")[0], len(data)
    inputData.append(data)
    inputName.append(filename.split("/")[-1].split(".")[0])

print len(inputData)

index = 0
for data in inputData:
    shuffle(data)
    pos = []
    neg = []

    for doc in data:
        label = doc.split('\t')[0]
        content = doc.split('\t')[1]
        if len(content) > 10:
            if label == '__label__pos' and len(pos) < 100:
                pos.append(doc)
            elif label == '__label__neg' and len(neg) < 100:
                neg.append(doc)

    docs = pos + neg
    shuffle(docs)
    out = ''
    for doc in docs:
        out += doc

    filename = outputFolder + "/" + inputName[index] + ".txt"
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filename, "w") as outFile:
        outFile.write(out)
    index += 1
