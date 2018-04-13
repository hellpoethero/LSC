import os
from random import shuffle

fold = 5
inputFolder1 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_1"
inputFolder2 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_2"
outputFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_3"
inputData = []
inputName = []
outputFiles = []

for filename in os.listdir(inputFolder2):
    filename = inputFolder2 + "/" + filename
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

    train_output = ""
    for line in data:
        train_output += line

    for i in range(0, fold):
        with open(inputFolder1 + "/" + inputName[index] + "/" + inputName[index] + "_train_" + str(i) + ".txt",
                  "r") as inputFile:
            temp_train_output = train_output
            for line in inputFile:
                temp_train_output += line

            if not os.path.exists(outputFolder + "/" + inputName[index]):
                os.makedirs(outputFolder + "/" + inputName[index])

            with open(outputFolder + "/" + inputName[index] + "/" + inputName[index] + "_train_" + str(i) + ".txt",
                      "a") as outputFile:
                outputFile.write(temp_train_output)
    index += 1
