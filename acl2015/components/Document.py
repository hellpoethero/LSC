class Document:
    def __init__(self, sentence, label):
        if len(sentence) > 0:
            self.words = sentence.split(' ')
        else:
            self.words = []
        self.sentence = sentence
        self.label = label
        pass
