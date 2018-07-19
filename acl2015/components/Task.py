import Document


class Task:
    def __init__(self):
        self.name = ""
        self.words = []
        self.docs = []
        self.docs_set = []
        self.values = []
        self.label_counts = [0, 0]
        self.label_prob = []

    def import_target(self, docs):
        self.docs = docs

        for doc in docs:
            label_num = 0
            if doc.label == '__label__pos':
                label_num = 0  # positive label
            elif doc.label == '__label__neg':
                label_num = 1  # negative label
            self.label_counts[label_num] += 1
            for word in doc.words:
                if word != '':
                    if word not in self.words:
                        value = WordValue()
                        self.words.append(word)
                        self.values.append(value)
                    word_index = self.words.index(word)
                    self.values[word_index].appear[label_num] += 1

        self.calculate_prob()
        self.label_prob = [float(self.label_counts[0]) / float(self.label_counts[0] + self.label_counts[1]),
                           float(self.label_counts[1]) / float(self.label_counts[0] + self.label_counts[1])]

    def import_file(self, filename):
        self.name = filename.split("/")[-1:][0]
        # comment vao de chay thu cach khac!
        # with open(filename + ".vocab", 'r') as vocabFile:
        #     self.import_vocab(vocabFile)
        # for i in range(0, 5):
        #     with open(filename + "_test_"+str(i)+".docs", 'r') as docsFile:
        #         self.import_docs(docsFile)

        for i in range(0, 5):
            with open(filename + "_test_"+str(i)+".txt", 'r') as txtFile:
                self.import_txt(txtFile)

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
        temp_docs = []
        for line in docs_file:
            if len(line.rstrip().split(":")) > 1:
                label = line.rstrip().split(":")[0]
                if label != 'neu':
                    sentence = line.rstrip().split(":")[1]
                    doc = Document.Document(sentence, label)
                    self.docs.append(doc)
                    temp_docs.append(doc)
                    if doc.label == 'pos':
                        label_num = 0  # positive label
                    elif doc.label == 'neg':
                        label_num = 1  # negative label
                    self.label_counts[label_num] += 1
                    for word in doc.words:
                        if word != '':
                            self.values[int(word)].appear[label_num] += 1
        self.docs_set.append(temp_docs)

    def import_txt(self, txt_file):
        temp_txt = []
        for line in txt_file:
            if len(line.rstrip().split("\t")) > 1:
                label = line.rstrip().split("\t")[0]
                if label != '__label__neu':
                    sentence = line.rstrip().split("\t")[1].rstrip()
                    doc = Document.Document(sentence, label)
                    self.docs.append(doc)
                    temp_txt.append(doc)
                    label_num = 0
                    if doc.label == '__label__pos':
                        label_num = 0  # positive label
                    elif doc.label == '__label__neg':
                        label_num = 1  # negative label
                    self.label_counts[label_num] += 1
                    for word in doc.words:
                        if word != '':
                            if word not in self.words:
                                value = WordValue()
                                self.words.append(word)
                                self.values.append(value)
                            word_index = self.words.index(word)
                            self.values[word_index].appear[label_num] += 1
        self.docs_set.append(temp_txt)

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
