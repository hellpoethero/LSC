class KnowledgeBase:
    def __init__(self, pis):
        self.words = []
        self.values = []
        self.convert(pis)
        print(self.words)
        print(self.values[0])
        print(self.values[1])

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

                    value.doc_pos += values_task[i].appear_pos
                    value.doc_neg += values_task[i].appear_neg
                    if values_task[i].prob_pos > values_task[i].prob_pos:
                        value.dom_pos += 1
                    else:
                        value.dom_neg += 1
                else:
                    index = self.words.index(word)
                    value = self.values[index]

                    value.doc_pos += values_task[i].appear_pos
                    value.doc_neg += values_task[i].appear_neg
                    if values_task[i].prob_pos > values_task[i].prob_pos:
                        value.dom_pos += 1
                    else:
                        if values_task[i].prob_pos < values_task[i].prob_pos:
                            value.dom_neg += 1
                i += 1


class WordKnowledge:
    def __init__(self):
        self.doc_pos = 0
        self.doc_neg = 0
        self.dom_pos = 0
        self.dom_neg = 0

    def __str__(self):
        return "%s %s %s %s" % (self.doc_pos, self.doc_neg, self.dom_pos, self.dom_neg)
