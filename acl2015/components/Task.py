class Task:
    def __init__(self):
        self.words = []
        self.values = []

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


class WordValue:
    def __init__(self):
        self.prob_pos = 0
        self.prob_neg = 0
        self.appear_pos = 0
        self.appear_neg = 0

    def __str__(self):
        return "%s %s %s %s" % (self.prob_pos, self.prob_neg, self.appear_pos, self.appear_neg)
