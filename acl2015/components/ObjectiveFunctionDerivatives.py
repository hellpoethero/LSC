class ObjectiveFunctionDerivatives:
    def __init__(self, smoothing, virtual_counts, task, learning_rate):
        self.smoothing = smoothing
        self.virtual_counts = virtual_counts
        self.label_prob = task.label_prob
        self.docs = task.docs
        self.vocab_size = len(task.words)
        self.learning_rate = learning_rate

    def optimize(self):
        for doc in self.docs:
            self.optimize_doc(doc)

    def optimize_doc(self, doc):
        word_set = set(doc.words)
        word_freq = []
        doc_len = len(doc.words)

        max_freq = 0
        for word in word_set:
            if max_freq < doc.words.count(word):
                max_freq = doc.words.count(word)

        for word in word_set:
            word_freq.append(float(doc.words.count(word) / max_freq))
        index = 0

        for word in word_set:
            self.optimize_word(word, index, word_set, word_freq, doc_len, doc.label)
            index += 1

    def optimize_word(self, word, index, word_set, word_freq, doc_len, label):
        freq = word_freq[index]
        virtual_count = self.virtual_counts[int(word)]

        a1 = freq / (self.smoothing + virtual_count[0])
        a2 = freq / (self.smoothing + virtual_count[1])
        b1 = self.label_prob[1] / self.label_prob[0] * self.mul_virtual_counts(word_set, word_freq, 0)
        b2 = self.label_prob[0] / self.label_prob[1] * self.mul_virtual_counts(word_set, word_freq, 1)
        c1 = self.g_derivatives()
        c2 = self.g_derivatives()
        g = self.g(doc_len)

        if label == 'pos':
            derivatives_pos = (a1 + b1 * c1) / (1 + b1 * g) - a1
            derivatives_neg = (a2*g + c2) / (b2 + g)
        elif label == 'neg':
            derivatives_pos = (a1 + b1 * c1) / (1 + b1 * g) - c1 / g
            derivatives_neg = (a2 * g + c2) / (b2 + g) - (a2 + c2/g)

    def g(self, doc_len):
        result = ((self.smoothing * self.vocab_size + self.sum_virtual_counts(0)) / (
                self.smoothing * self.vocab_size + self.sum_virtual_counts(1))) ** doc_len
        return result

    def g_derivatives(self):
        return 1

    def sum_virtual_counts(self, label_num):
        sum_virtual_counts = 0
        for value in self.virtual_counts:
            sum_virtual_counts += value[label_num]
        return sum_virtual_counts

    def mul_virtual_counts(self, words, word_freq, label_num):
        mul_virtual_counts = 1
        index = 0
        for word in words:
            mul_virtual_counts *= ((self.smoothing + self.virtual_counts[int(word)][1-label_num]) / (
                    self.smoothing + self.virtual_counts[int(word)][label_num])) ** word_freq[index]
            index += 1
        return mul_virtual_counts
