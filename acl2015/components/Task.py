import Document


class Task:
    def __init__(self, filename):
        self.words = []
        self.docs = []
        self.values = []
        with open(filename+".vocab", 'r') as vocabFile:
            self.import_vocab(vocabFile)
        with open(filename+".docs", 'r') as docsFile:
            self.import_docs(docsFile)
        self.calculate_prob()

    def import_vocab(self, vocab_file):
        for line in vocab_file:
            word = line.split(":")[1].rstrip()
            value = WordValue()

            self.words.append(word)
            self.values.append(value)

    def import_prob(self, prob_file):
        i = 0
        for line in prob_file:
            pos = line.split(":")[0]
            neg = line.split(":")[1]

            self.values[i].prob_pos = float(pos)
            self.values[i].prob_neg = float(neg)
            i = i+1

    def import_appear(self, appear_file):
        i = 0
        for line in appear_file:
            pos = line.split(":")[0]
            neg = line.split(":")[1]

            self.values[i].appear_pos = int(pos)
            self.values[i].appear_neg = int(neg)
            i = i+1

    def import_docs(self, docs_file):
        for line in docs_file:
            label = line.rstrip().split(":")[0]
            sentence = line.rstrip().split(":")[1]
            doc = Document.Document(sentence, label)
            self.docs.append(doc)
            if doc.label == 'pos':
                for word in doc.words:
                    self.values[int(word)].appear_pos += 1
            else:
                for word in doc.words:
                    self.values[int(word)].appear_neg += 1

    def calculate_prob(self):
        total_appear_pos = 0
        total_appear_neg = 0
        for word in self.values:
            total_appear_pos += word.appear_pos
            total_appear_neg += word.appear_neg
        for word in self.values:
            word.calculate_prob(1, len(self.words), total_appear_pos, total_appear_neg)


class WordValue:
    def __init__(self):
        self.prob_pos = 0
        self.prob_neg = 0
        self.appear_pos = 0
        self.appear_neg = 0

    def calculate_prob(self, smoothing, vocab_size, total_appear_pos, total_appear_neg):
        self.prob_pos = float(smoothing + self.appear_pos) / float(smoothing * vocab_size + total_appear_pos)
        self.prob_neg = float(smoothing + self.appear_neg) / float(smoothing * vocab_size + total_appear_neg)

    def __str__(self):
        return "word value: %s %s %s %s" % (self.prob_pos, self.prob_neg, self.appear_pos, self.appear_neg)
