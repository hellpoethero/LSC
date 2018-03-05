class KnowledgeBase:
    def __init__(self):
        self.words = []
        self.values = []

    def convert(self, pis):
        for task in pis.tasks:
            words_task = task.words
            values_task = task.values
            i = 0
            for word in words_task:
                if word not in self.words:
                    self.words.append(word)
                    value = WordKnowledge()

                    self.values.append(value)
                else:
                    index = self.words.index(word)
                    value = self.values[index]

                value.doc[0] += values_task[i].appear[0]
                value.doc[1] += values_task[i].appear[1]

                if values_task[i].prob[0] > values_task[i].prob[1]:
                    value.dom[0] += 1
                elif values_task[i].prob[0] < values_task[i].prob[1]:
                    value.dom[1] += 1
                i += 1
        print "Init Knowledge Base"


class WordKnowledge:
    def __init__(self):
        self.doc = [0, 0]
        self.dom = [0, 0]

    def __str__(self):
        return "word knowledge: %s %s %s %s" % (self.doc[0], self.doc[1], self.dom[0], self.dom[1])
