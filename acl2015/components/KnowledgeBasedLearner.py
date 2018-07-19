import time
import os


class KnowledgeBaseLearner:
    def __init__(self, close, target, km, task_index, smoothing, learning_rate, threshold_1, threshold_2, reg_co):
        if close == 0:
            self.kb = km.past_kb
        else:
            self.kb = km.close_kb
        self.target = target
        self.label_prob = self.target.label_prob
        self.smoothing = smoothing
        self.virtual_counts = []
        self.starting_points = []
        self.label_prob = self.target.label_prob
        self.docs = self.target.docs
        self.vocab_size = len(self.target.words)
        self.learning_rate = learning_rate
        self.vt = []
        self.vs = []
        self.reg_co = reg_co
        self.target = target
        self.task_index = task_index

        print len(self.target.docs), len(self.target.words)
        print len(self.kb.words)

        document_knowledge = []
        domain_knowledge = []

        index = 0
        for word in self.target.words:
            if word in self.kb.words:
                word_index = self.kb.words.index(word)
                doc = self.kb.values[word_index].doc
                dom = self.kb.values[word_index].dom
            else:
                doc = [0, 0]
                dom = [0, 0]

            document_knowledge.append(doc)
            domain_knowledge.append(dom)

            # starting point
            self.starting_points.append(doc)
            # virtual counts
            appear = self.target.values[index].appear
            virtual_count = [doc[0] + appear[0],
                             doc[1] + appear[1]]
            self.virtual_counts.append(virtual_count)
            # print word, doc, appear, virtual_count

            a = float(self.target.values[index].prob[0]) / float(self.target.values[index].prob[1])
            b = float(self.target.values[index].prob[1]) / float(self.target.values[index].prob[0])
            # print word, self.task.values[index].prob, self.task.values[index].appear, a, b
            if a >= threshold_1 or b >= threshold_1:
                self.vt.append(index)
                # print word, a, b
            if word in self.kb.words:
                # dom = domain_knowledge[index]
                if dom[0] >= threshold_2 or dom[1] >= threshold_2:
                    self.vs.append(index)
                    # print word, dom
            index += 1

        # print 'Number of word: ', len(self.virtual_counts)
        self.virtual_probs = self.calculate_prob()
        self.folder = ''

    def set_output_folder(self, folder):
        self.folder = folder

    def get_nb_model(self):
        folder = self.folder + '_nb'
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' +
                  self.target.name + '_' + str(self.task_index) + '.nb.model', 'a+') as model:
            model.write(str(self.smoothing) + '\n')
            model.write(str(self.label_prob[0]) + ' ' + str(self.label_prob[1]) + '\n')
            index = 0
            for word in self.target.words:
                model.write(word + ':' + str(self.target.values[index].appear[0]) + ' ' + str(
                    self.target.values[index].appear[1]) + '\n')
                index += 1
            model.close()

    def get_nb_past_model(self):
        folder = self.folder + '_nb'
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' +
                  self.target.name + '.nb.model', 'a+') as model:
            model.write(str(self.smoothing) + '\n')
            model.write(str(self.label_prob[0]) + ' ' + str(self.label_prob[1]) + '\n')
            index = 0
            for word in self.target.words:
                model.write(word + ':' + str(self.target.values[index].appear[0]) + ' ' + str(
                    self.target.values[index].appear[1]) + '\n')
                index += 1
            model.close()

    def objective_function(self, doc, word_freq):
        virtual_probs = self.calculate_prob()
        word_set = set(doc.words)
        total = [self.label_prob[0], self.label_prob[1]]

        # print doc.words, doc.sentence
        for label_index in [0, 1]:
            i = 0
            for word in word_set:
                if word != '':
                    word_index = self.target.words.index(word)
                    total[label_index] *= virtual_probs[word_index][label_index] ** word_freq[i]
                    i += 1

        pos = total[0] / (total[0] + total[1])
        neg = total[1] / (total[0] + total[1])
        if doc.label == '__label__pos':
            result = pos - neg
        else:
            result = neg - pos
        # print pos, neg
        return result

    def optimize(self):
        # print "Optimize"
        index = 0
        print self.label_prob
        for doc in self.docs:
            print "optimize doc", index, doc.label, self.target.name + str(self.task_index)
            self.optimize_doc(doc)
            index += 1
            print "\n"
            # break
        folder = self.folder + '_lsc'
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' + self.target.name+'_' + str(self.task_index) + '.lsc.model', 'a+') as model:
            model.write(str(self.smoothing)+'\n')
            model.write(str(self.label_prob[0])+' '+str(self.label_prob[1])+'\n')
            index = 0
            for word in self.target.words:
                model.write(word+':'+str(self.virtual_counts[index][0])+' '+str(self.virtual_counts[index][1])+'\n')
                index += 1
            model.close()

    def optimize_doc(self, doc):
        word_set = set(doc.words)
        word_freq = []
        doc_len = len(doc.words)

        for word in word_set:
            word_freq.append(float(doc.words.count(word)) / doc_len)

        # print word_set
        # print self.objective_function(doc, word_freq)
        index = 0
        for word in word_set:
            if word != '':
                print "optimize", word
                self.optimize_word(word, index, word_set, word_freq, doc_len, doc.label, doc)
                index += 1
                print "---------------------------"
            # break

    def optimize_word(self, word, index, word_set, word_freq, doc_len, label, doc):
        word_index = self.target.words.index(word)
        freq = word_freq[index]
        virtual_count = self.virtual_counts[word_index]

        current_obj_f = self.objective_function(doc, word_freq)

        i = 0
        while 1:
            print virtual_count
            a1 = freq / (self.smoothing + virtual_count[0])
            a2 = freq / (self.smoothing + virtual_count[1])
            b1 = float(self.label_prob[1]) / float(self.label_prob[0]) * self.mul_virtual_counts(word_set, word_freq, 0)
            b2 = float(self.label_prob[0]) / float(self.label_prob[1]) * self.mul_virtual_counts(word_set, word_freq, 1)
            c1 = self.g_derivatives(0, doc_len)
            c2 = self.g_derivatives(1, doc_len)
            g = self.g(doc_len)

            vs = [0, 0]
            if word_index in self.vs:
                vs = self.calculate_vs_derivatives()

            vt = [0, 0]
            if word_index in self.vt:
                vt = self.calculate_vt_derivatives()

            derivatives_pos = 0
            derivatives_neg = 0
            if label == '__label__pos':
                derivatives_pos = (a1 + b1 * c1) / (1 + b1 * g) - a1 + vt[0] + vs[0]
                derivatives_neg = (a2 * g + c2) / (b2 + g) + vt[1] + vs[1]
            elif label == '__label__neg':
                derivatives_pos = (a1 + b1 * c1) / (1 + b1 * g) - c1 / g + vt[0] + vs[0]
                derivatives_neg = (a2 * g + c2) / (b2 + g) - (a2 + c2 / g) + vt[1] + vs[1]

            # print a1, b1, c1, g, virtual_count, vt, vs, derivatives_pos, derivatives_neg
            print derivatives_pos, derivatives_neg

            # for word in word_set:
            #     print self.virtual_counts[int(word)]

            pos_flag = 0
            neg_flag = 0
            if virtual_count[0] - self.learning_rate * derivatives_pos > 0:
                virtual_count[0] -= self.learning_rate * derivatives_pos
                pos_flag = 1
            if virtual_count[1] - self.learning_rate * derivatives_neg > 0:
                virtual_count[1] -= self.learning_rate * derivatives_neg
                neg_flag = 1

            print virtual_count

            new_obj_f = self.objective_function(doc, word_freq)
            different = (new_obj_f - current_obj_f)
            print current_obj_f, new_obj_f, different

            if different < 10 ** -3:
                if pos_flag == 1:
                    virtual_count[0] += self.learning_rate * derivatives_pos
                if neg_flag == 1:
                    virtual_count[1] += self.learning_rate * derivatives_neg
                break
            # print virtual_count
            current_obj_f = new_obj_f
            i += 1
            # break

    # cong thuc 4, tinh g(X)
    def g(self, doc_len):
        pos = float(self.smoothing * self.vocab_size + self.sum_virtual_counts(0))
        neg = float(self.smoothing * self.vocab_size + self.sum_virtual_counts(1))
        a = pos / neg
        # print "g", self.sum_virtual_counts(0), self.sum_virtual_counts(1), self.smoothing, a
        result = a ** doc_len
        return result

    # dao ham cong thuc 4 g(X)
    def g_derivatives(self, label_num, doc_len):
        pos_sum = self.sum_virtual_counts(0)
        neg_sum = self.sum_virtual_counts(1)
        pos = float(self.smoothing * self.vocab_size + pos_sum)
        neg = float(self.smoothing * self.vocab_size + neg_sum)

        # print pos_sum, neg_sum

        if label_num == 0:
            result = doc_len * (pos / neg) ** (doc_len - 1) * (1 / neg)
        else:
            result = doc_len * (pos / neg) ** (doc_len - 1) * (-pos / neg ** 2)
        return result

    def sum_virtual_counts(self, label_num):
        sum_virtual_counts = 0
        for value in self.virtual_counts:
            sum_virtual_counts += value[label_num]
        return sum_virtual_counts

    def mul_virtual_counts(self, words, word_freq, label_num):
        mul_virtual_counts = 1
        index = 0
        for word in words:
            word_index = self.target.words.index(word)
            a = float(self.smoothing + self.virtual_counts[word_index][1 - label_num]) / float(
                self.smoothing + self.virtual_counts[word_index][label_num])
            mul_virtual_counts *= a ** word_freq[index]
            # print word, word_freq[index], self.virtual_counts[word_index][1 - label_num], \
            #     self.virtual_counts[word_index][label_num], a, a ** word_freq[index]
            index += 1
        # print mul_virtual_counts
        return mul_virtual_counts

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
                    float(self.smoothing + value[i]) / float(self.smoothing * self.vocab_size + total_virtual_count[i]))
            virtual_probs.append(virtual_prob)
        return virtual_probs

    def calculate_label(self, doc):
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
                if word in self.target.words:
                    # print word, self.task.words.index(word)
                    total[label_index] *= self.virtual_probs[self.target.words.index(word)][label_index] ** word_freq[i]
            i += 1

        # print total[0], total[1]
        if total[0] + total[1] > 0:
            pos = total[0] / (total[0] + total[1])
            neg = total[1] / (total[0] + total[1])

            # print pos, neg
            if pos > neg:
                # print 'pos'
                return 'pos'
            else:
                # print 'neg'
                return 'neg'
        else:
            # print 'neu'
            return 'neu'

    def calculate_vs_derivatives(self):
        a = [0, 0]
        for word_index in self.vs:
            dom = self.kb.values[self.kb.words.index(self.target.words[word_index])].dom
            c = float(dom[0]) / float(dom[0] + dom[1])
            # print self.virtual_counts[word_index], self.starting_points[word_index]
            a[0] += (float(self.virtual_counts[word_index][0]) - c * float(self.starting_points[word_index][0]))
            a[1] += (float(self.virtual_counts[word_index][1]) - (1 - c) * float(self.starting_points[word_index][1]))

        a[0] *= self.reg_co
        a[1] *= self.reg_co
        # print 'vs', a
        return a

    def calculate_vt_derivatives(self):
        a = [0, 0]
        for word_index in self.vt:
            a[0] += (self.virtual_counts[word_index][0] - self.target.values[word_index].appear[0])
            a[1] += (self.virtual_counts[word_index][1] - self.target.values[word_index].appear[1])
        a[0] *= self.reg_co
        a[1] *= self.reg_co
        print 'vt', a
        return a
