class Test:
    def __init__(self, kbl, test_data, words):
        self.kbl = kbl
        self.test_data = test_data
        self.words = words
        self.true_pos = 0
        self.true_neg = 0
        self.false_pos = 0
        self.false_neg = 0

    def run_test(self):
        for doc in self.test_data:
            sentence = ""
            for word in doc.words:
                sentence += self.words[int(word)] + " "
            label = self.kbl.calculate_label(sentence)

            if label == 'pos':
                if label == doc.label:
                    self.true_pos += 1
                else:
                    self.false_pos += 1
            else:
                if label == doc.label:
                    self.true_neg += 1
                else:
                    self.false_neg += 1
