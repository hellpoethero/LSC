import os
from os.path import basename

inputFolder = "abc"
outputFiles = []

for subFolder in os.listdir(inputFolder):
    outputFileName = "abc_1/" + basename(inputFolder + "/" + subFolder)
    outputFiles.append(outputFileName)
    with open(outputFileName, "w") as outputFile:
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

