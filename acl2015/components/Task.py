import Document


class Task:
    def __init__(self, filename):
        self.name = filename.split("/")[-1:][0]
        self.words = []
        self.docs = []
        self.values = []
        self.label_counts = [0, 0]
        with open(filename + ".vocab", 'r') as vocabFile:
            self.import_vocab(vocabFile)
        with open(filename + ".docs", 'r') as docsFile:
            self.import_docs(docsFile)
        self.calculate_prob()
        self.label_prob = [float(self.label_counts[0]) / float(self.label_counts[0] + self.label_counts[1]),
                           float(self.label_counts[1]) / float(self.label_counts[0] + self.label_counts[1])]

    def import_vocab(self, vocab_file):
        for line in vocab_file:
            word = line.split(":")[1].rstrip()
            value = WordValue()

            self.words.append(word)
            self.values.append(value)

    def import_docs(self, docs_file):
        for line in docs_file:
            label = line.rstrip().split(":")[0]
            if label != 'neu':
                sentence = line.rstrip().split(":")[1]
                doc = Document.Document(sentence, label)
                self.docs.append(doc)
                if doc.label == 'pos':
                    label_num = 0  # positive label
                elif doc.label == 'neg':
                    label_num = 1  # negative label
                self.label_counts[label_num] += 1
                for word in doc.words:
                    if word != '':
                        self.values[int(word)].appear[label_num] += 1

    def calculate_prob(self):
        total_appear = [0, 0]
        for word in self.values:
            total_appear[0] += word.appear[0]
            total_appear[1] += word.appear[1]
        for word in self.values:
            word.calculate_prob(1, len(self.words), total_appear)


class WordValue:
    def __init__(self):
        self.prob = [0, 0]
        self.appear = [0, 0]

    def calculate_prob(self, smoothing, vocab_size, total_appear):
        for i in [0, 1]:
            self.prob[i] = float(smoothing + self.appear[i]) / float(smoothing * vocab_size + total_appear[i])

    def __str__(self):
        return "word value: %s %s %s %s" % (self.prob[0], self.prob[1], self.appear[0], self.appear[1])
