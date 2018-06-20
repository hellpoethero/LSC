import os
from os.path import basename

inputFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_100"
outputFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_100_2/"
outputFiles = []

for subFolder in os.listdir(inputFolder):
    domain_name = basename(inputFolder + "/" + subFolder).split('.')[0]
    outputFileName = outputFolder + domain_name
    outputFiles.append(outputFileName + "/" + domain_name + ".txt")
    if not os.path.exists(outputFileName):
        os.makedirs(outputFileName)
    print outputFileName
    with open(outputFileName + "/" + domain_name + ".txt", "w") as outputFile:
        outputFile.write("")

print len(outputFiles)

index = 0
for subFolder in os.listdir(inputFolder):
    filename = inputFolder + "/" + subFolder
    # print filename
    with open(filename, "r") as inputFile:
        out = ""
        for line in inputFile:
            # print line
            out += line
        index1 = 0
        for outputFileName in outputFiles:
            if index != index1:
                with open(outputFileName, "a") as outputFile:
                    outputFile.write(out)
            index1 += 1

        print(basename(filename))
        index += 1

