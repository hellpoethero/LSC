class Document:
    def __init__(self, sentence, label):
        self.words = []
        if len(sentence) > 0:
            words = sentence.rstrip().split(' ')
            for word in words:
                if word != '':
                    self.words.append(word)
        self.sentence = sentence
        self.label = label
        pass
