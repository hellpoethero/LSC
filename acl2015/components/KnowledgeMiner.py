import PastInformationStore
import KnowledgeBase


class KnowledgeMiner:
    def __init__(self, folder_name):
        self.pis = PastInformationStore.PastInformationStore()
        self.pis.read_from_folder(folder_name)
        self.kb = KnowledgeBase.KnowledgeBase()
        self.kb.convert(self.pis)

        self.close_kb = KnowledgeBase.KnowledgeBase()

        self.current_task_index = -1

    def set_close_kb(self, sort_domains, num):
        pis = PastInformationStore.PastInformationStore()
        with open('C:/Users/dennis hell/Desktop/LSC/close_domain.txt', 'a') as close_domain_file:
            # close_domain_file.write('domain: ' + self.pis.tasks[self.current_task_index].name + '\n')
            for i in range(0, num):
                pis.tasks.append(self.pis.tasks[sort_domains[i]])
                # print self.pis.tasks[sort_domains[i]].name
                # close_domain_file.write(self.pis.tasks[sort_domains[i]].name + '\n')
            # close_domain_file.write('----------')
            self.close_kb = KnowledgeBase.KnowledgeBase()
            self.close_kb.convert(pis)

    def set_current_task(self, current_task_index):
        if current_task_index >= 0 & current_task_index < len(self.pis.tasks):
            self.current_task_index = current_task_index

    def get_current_task(self):
        if self.current_task_index >= 0 & self.current_task_index < len(self.pis.tasks):
            return self.pis.tasks[self.current_task_index]

