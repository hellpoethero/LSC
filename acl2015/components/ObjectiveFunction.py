class ObjectiveFunction:
    def __init__(self, task):
        self.task = task
        pass

    def calculate(self):
        ofs = []
        i = 0
        for doc in self.task.docs:
            doc_len = len(doc.words)
            word_set = set(doc.words)
            word_freq = []
            for word in word_set:
                word_freq.append(float(doc.words.count(word)) / doc_len)
            ofs.append(self.calculate_doc(doc.label, word_freq, word_set))
            i += 1
        return ofs

    def calculate_doc(self, label, word_freq, word_set):
        total = [self.task.label_prob[0], self.task.label_prob[1]]

        for label_index in [0, 1]:
            i = 0
            for word in word_set:
                total[label_index] *= self.task.values[int(word)].prob[label_index] ** word_freq[i]
                i += 1

        pos = total[0] / (total[0] + total[1])
        neg = total[1] / (total[0] + total[1])
        if label == 'pos':
            result = pos - neg
        else:
            result = neg - pos
        # print pos, neg
        return result
