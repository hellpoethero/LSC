import PastInformationStore
import KnowledgeBase


class KnowledgeMiner:
    def __init__(self, folder_name):
        self.pis = PastInformationStore.PastInformationStore(folder_name)
        self.kb = KnowledgeBase.KnowledgeBase()
        self.kb.convert(self.pis)
        self.current_task_index = -1
        pass

    def set_current_task(self, current_task_index):
        if current_task_index >= 0 & current_task_index < len(self.pis.tasks):
            self.current_task_index = current_task_index

    def get_current_task(self):
        if self.current_task_index >= 0 & self.current_task_index < len(self.pis.tasks):
            return self.pis.tasks[self.current_task_index]

