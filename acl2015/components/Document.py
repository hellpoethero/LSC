class Document:
    def __init__(self, sentence, label):
        if len(sentence) > 0:
            self.words = sentence.split(' ')
        else:
            self.words = []
        self.label = label
        pass
