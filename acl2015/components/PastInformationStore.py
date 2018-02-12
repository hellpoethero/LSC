import os
import Task


class PastInformationStore:
    def __init__(self, folder_name):
        self.tasks = []
        self.read_from_folder(folder_name)
        pass

    def read_from_folder(self, folder_name):
        for subFolderName in os.listdir(folder_name):
            filename = folder_name + "/" + subFolderName+"/"+subFolderName
            task = Task.Task()
            with open(filename+".vocab", 'r') as vocabFile:
                task.import_vocab(vocabFile)
            with open(filename+".prob", 'r') as probFile:
                task.import_prob(probFile)
            with open(filename+".appear", 'r') as appearFile:
                task.import_appear(appearFile)
            self.tasks.append(task)
        print len(self.tasks)
        print self.tasks[0].values[0]
        print self.tasks[0].values[1]
