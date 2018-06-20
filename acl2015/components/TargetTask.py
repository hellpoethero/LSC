from random import shuffle
import Task


class TargetTask:
    def __init__(self, task, fold):
        self.task = task
        self.fold = fold
        self.words = task.words

    def get_target_task(self, fold_number):
        docs = []
        for i in range(0, self.fold):
            if i != fold_number:
                docs += self.task.docs_set[i]
        task = Task.Task()
        task.import_target(docs, self.words)
        return task

    def get_test_data(self, fold_number):
        return self.task.docs_set[fold_number]
