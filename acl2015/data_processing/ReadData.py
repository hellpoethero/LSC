import os
from ..components import Document


class ReadData:
    def __init__(self):
        pass

    def read_folder(self, folder_name):
        domains = []
        for subFolderName in os.listdir(folder_name):
            filename = folder_name + "/" + subFolderName + "/" + subFolderName
            domains.append(self.read_sub_folder(filename))
        return domains

    @staticmethod
    def read_sub_folder(filename):
        with open(filename + ".txt", "r") as txtFile:
            txtFile.readline()
            docs = []
            for line in txtFile:
                label_num = line.replace("\n", "").split("\t")[0]
                if int(label_num) > 3:
                    label = 'pos'
                elif int(label_num) < 3:
                    label = 'neg'
                else:
                    label = 'neu'
                # labels.append(label)
                content = line.lower().replace("\n", "").split("\t")[1]
                # words_line = content[:len(content)-1].split(" ")
                doc = Document.Document(content[:len(content)-1], label)
                docs.append(doc)
                # words += words_line
                # docs.append(words_line)
        return docs
