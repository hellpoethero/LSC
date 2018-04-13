import os
from random import shuffle

fold = 5
inputFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc"
outputFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_1"
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
    for i in range(0, fold):
        size = len(data) / fold
        test_data = data[i * size:(i + 1) * size]
        train_data = data[0:i * size] + data[(i + 1) * size:len(data)]

        test_output = ""
        train_output = ""
        for line in test_data:
            test_output += line
        for line in train_data:
            train_output += line

        if not os.path.exists(outputFolder + "/" + inputName[index]):
            os.makedirs(outputFolder + "/" + inputName[index])

        with open(outputFolder + "/" + inputName[index] + "/" + inputName[index] + "_test_" + str(i) + ".txt",
                  "a") as outputFile:
            outputFile.write(test_output)

        with open(outputFolder + "/" + inputName[index] + "/" + inputName[index] + "_train_" + str(i) + ".txt",
                  "a") as outputFile:
            outputFile.write(train_output)
    index += 1
