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
        task.name = self.task.name
        task.import_target(docs)
        return task

    def get_target_task_from_past(self, tasks, task_index):
        docs = []
        i = 0
        for task in tasks:
            if i != task_index:
                docs += task.docs
            i += 1
        task = Task.Task()
        task.name = self.task.name
        task.import_target(docs)
        return task

    def get_target_task_from_past_and_current(self, tasks, task_index, fold_number):
        docs = []
        i = 0
        for task in tasks:
            if i != task_index:
                docs += task.docs
            i += 1

        for i in range(0, self.fold):
            if i != fold_number:
                docs += self.task.docs_set[i]
        task = Task.Task()
        task.name = self.task.name
        task.import_target(docs)
        return task

    def get_test_data(self, fold_number):
        return self.task.docs_set[fold_number]
