class Model:
    def __init__(self, filename):
        with open(filename, 'r') as modelFile:
            self.smoothing = int(modelFile.readline())
            # print self.smoothing
            label_prob = modelFile.readline().split(' ')
            self.label_prob = [
                float(label_prob[0]),
                float(label_prob[1])]
            # print self.label_prob
            self.words = []
            self.virtual_counts = []
            for line in modelFile:
                word = line.split(':')[0]
                self.words.append(word)
                virtual_count_str = line.split(':')[1].split(' ')
                virtual_count = [float(virtual_count_str[0]), float(virtual_count_str[1])]
                self.virtual_counts.append(virtual_count)
                # print virtual_count
            self.virtual_probs = self.calculate_prob()

    def calculate_prob(self):
        total_virtual_count = [0, 0]
        virtual_probs = []
        for value in self.virtual_counts:
            total_virtual_count[0] += value[0]
            total_virtual_count[1] += value[1]
        # print total_virtual_count
        for value in self.virtual_counts:
            virtual_prob = []
            for i in [0, 1]:
                virtual_prob.append(
                    float(self.smoothing + value[i]) / float(self.smoothing * len(self.words) + total_virtual_count[i]))
            virtual_probs.append(virtual_prob)
        return virtual_probs

    def predict_label(self, doc):
        words = doc.rstrip().split(" ")
        word_set = set(words)
        word_freq = []
        doc_len = len(words)
        for word in word_set:
            word_freq.append(float(words.count(word)) / doc_len)

        # virtual_probs = self.calculate_prob()
        total = [self.label_prob[0], self.label_prob[1]]

        # print self.task.words
        # print word_set
        for label_index in [0, 1]:
            i = 0
            for word in word_set:
                if word in self.words:
                    # print word, self.task.words.index(word)
                    total[label_index] *= self.virtual_probs[self.words.index(word)][label_index] ** word_freq[i]
            i += 1

        # print total[0], total[1]
        if total[0] + total[1] > 0:
            pos = total[0] / (total[0] + total[1])
            neg = total[1] / (total[0] + total[1])

            # print pos, neg
            if pos > neg:
                # print 'pos'
                return '__label__pos'
            else:
                # print 'neg'
                return '__label__neg'
        else:
            # print 'neu'
            return '__label__neu'
