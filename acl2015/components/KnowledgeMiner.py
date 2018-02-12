import PastInformationStore
import KnowledgeBase


class KnowledgeMiner:
    def __init__(self, folder_name):
        self.pis = PastInformationStore.PastInformationStore(folder_name)
        self.kb = KnowledgeBase.KnowledgeBase(self.pis)
        pass
