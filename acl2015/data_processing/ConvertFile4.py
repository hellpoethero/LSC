import os


inputFolder1 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb_100_5"
inputFolder2 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_100_1"
outputFolder1 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb_100_5_train"
outputFolder2 = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb_100_5_test"

index = 1
for subFolderName in os.listdir(inputFolder1):
    if index < 16:
        vocabsFileName = inputFolder1 + "/" + subFolderName + "/" + subFolderName + ".vocab"
        subFolder2 = inputFolder2 + "/" + subFolderName

        with open(vocabsFileName, "r") as vocabsFile:
            vocabs = []
            for line in vocabsFile:
                word = line.rstrip().split(":")[1]
                vocabs.append(word)
                # print word

            subOutputFolder1 = outputFolder1+"/"+subFolderName
            subOutputFolder2 = outputFolder2+"/"+subFolderName
            if not os.path.exists(subOutputFolder1):
                os.makedirs(subOutputFolder1)
            if not os.path.exists(subOutputFolder2):
                os.makedirs(subOutputFolder2)

            for subFolderName2 in os.listdir(subFolder2):
                with open(subFolder2+"/"+subFolderName2, "r") as xxx:
                    out = ""
                    for line in xxx:
                        # print line
                        abc = line.rstrip().split("\t")
                        label = line.rstrip().split("\t")[0]

                        if len(abc) > 1:
                            content = line.rstrip().split("\t")[1]

                            out += label[-3:] + ":"

                            words = content.split(" ")
                            for word in words:
                                out += str(vocabs.index(word)) + " "

                        out += "\n"
                    # print out

                    if "_test_" in subFolderName2:
                        print subOutputFolder2+"/"+subFolderName2[:-3]+"docs"
                        with open(subOutputFolder2+"/"+subFolderName2[:-3]+"docs", "w") as outFile:
                            outFile.write(out)
                    else:
                        print subOutputFolder1+"/"+subFolderName2[:-3]+"docs"
                        with open(subOutputFolder1+"/"+subFolderName2[:-3]+"docs", "w") as outFile:
                            outFile.write(out)
    index += 1

