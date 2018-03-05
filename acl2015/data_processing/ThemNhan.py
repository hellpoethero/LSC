import os


def read_from_folder(folder_name):
    for subFolderName in os.listdir(folder_name):
        filename = folder_name + "/" + subFolderName + "/" + subFolderName
        labels = []
        # with open(filename + ".txt", 'r') as txtFile:
        #     txtFile.readline()
        #     for line in txtFile:
        #         label = line.split("\t")[0]
        #         if int(label) > 3:
        #             labels.append("pos")
        #         elif int(label) < 3:
        #             labels.append("neg")
        #         else:
        #             labels.append("neu")
        output = ""
        with open(filename + ".docsx", 'r') as docsFile:
            index = 0
            for line in docsFile:
                # output += labels[index]+":"+line
                output += line
                index += 1
        with open(filename + ".docs", "w") as outFile:
                outFile.write(output)


read_from_folder("G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb")
