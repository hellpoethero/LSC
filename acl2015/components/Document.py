class Document:
    def __init__(self, sentence, label):
        self.words = sentence.split(' ')
        self.label = label
        pass
