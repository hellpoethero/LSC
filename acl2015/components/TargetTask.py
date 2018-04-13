from random import shuffle
import Task


class TargetTask:
    def __init__(self, task, fold):
        self.task = task
        self.docs = task.docs[:]
        self.words = task.words[:]
        shuffle(self.docs)
        self.fold = fold

    def get_train_data(self):
        test_size = len(self.docs) / self.fold
        train_data = []
        for i in range(0, self.fold):
            docs = self.docs[0:i*test_size] + self.docs[(i+1)*test_size:len(self.docs)]
            task = Task.Task()
            task.import_target(docs, self.words)
            train_data.append(task)
        return train_data

    def get_test_data(self):
        test_size = len(self.docs) / self.fold
        test_data = []
        for i in range(0, self.fold):
            test_data.append(self.docs[i*test_size:(i+1)*test_size])
        return test_data
