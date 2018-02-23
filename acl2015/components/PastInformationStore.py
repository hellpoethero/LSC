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
            self.read_from_sub_folder(filename)
        print 'number of task: ', len(self.tasks)
        print self.tasks[0].values[0]
        print self.tasks[0].values[88]

    def read_from_sub_folder(self, filename):
        task = Task.Task(filename)
        # with open(filename+".vocab", 'r') as vocabFile:
        #     task.import_vocab(vocabFile)
        # with open(filename+".docs", 'r') as docsFile:
        #     task.import_docs(docsFile)
        self.tasks.append(task)
