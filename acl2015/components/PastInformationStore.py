import os
import Task


class PastInformationStore:
    def __init__(self):
        self.tasks = []
        pass

    def read_from_folder(self, folder_name):
        for subFolderName in os.listdir(folder_name):
            filename = folder_name + "/" + subFolderName + "/" + subFolderName
            self.read_from_sub_folder(filename)
        print 'number of task: ', len(self.tasks)

    def read_from_sub_folder(self, filename):
        task = Task.Task()
        task.import_file(filename)
        self.tasks.append(task)
