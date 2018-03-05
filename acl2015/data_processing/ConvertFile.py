import math, os


def read_from_folder(folder_name):
    stop_list = []
    with open("G:\Hoc tap\NCKH\KT Lab\LifeLongLearning\code\LSC\sample_data\stopword1.txt", "r") as stopListFile:
        for line in stopListFile:
            stop_list.append(line[:len(line) - 1])

    # print stop_list
    stop_set = set(stop_list)

    for subFolderName in os.listdir(folder_name):
        filename = folder_name + "/" + subFolderName + "/" + subFolderName
        convert(filename, stop_set)


def convert(filename, stop_set):
    with open(filename+".txt", "r") as txtFile:
        txtFile.readline()
        words = []
        docs = []
        labels = []
        tf_idf_matrix = []
        word_tf_idf_sum = []
        word_important = []
        word_tf_idf_avg = []
        idfs = []
        for line in txtFile:
            label = line.replace("\n", "").split("\t")[0]
            labels.append(label)
            content = line.lower().replace("\n", "").split("\t")[1]
            words_line = content[:len(content)-1].split(" ")
            words += words_line
            docs.append(words_line)

        word_set = set(words)
        print len(words), len(word_set)
        vocab = []
        vocab += word_set

        words_count = []
        word_doc_count = []
        for word in vocab:
            count = words.count(word)
            words_count.append(0)
            word_doc_count.append(0)
            word_tf_idf_avg.append(0)
            word_tf_idf_sum.append(0)

        for doc in docs:
            word_doc_set = set(doc)
            for word in word_doc_set:
                word_index = vocab.index(word)
                word_doc_count[word_index] += 1
                words_count[word_index] += doc.count(word)

        avg_v = 0
        avg_v_1 = 0
        max_v = 0
        min_v = 0
        index = 0
        index_1 = 0
        docs_len = len(docs)
        for doc in docs:
            word_doc_set = set(doc)
            doc_len = len(doc)
            tf_idf_doc = []
            for word in word_doc_set:
                word_index = vocab.index(word)
                word_count = doc.count(word)
                tf = float(word_count) / float(doc_len)
                idf = math.log1p(float(docs_len) / float(word_doc_count[word_index]))
                a = tf * idf
                avg_v += a
                index += 1
                if a > 0:
                    avg_v_1 += a
                    index_1 += 1
                if a > max_v:
                    max_v = a
                if a < min_v:
                    min_v = a
                # print word, words_count[word_index], word_doc_count[word_index], doc_len, a, tf, idf
                word_tf_idf_sum[word_index] += a
                tf_idf_doc.append(a)
            # print "----------"
            tf_idf_matrix.append(tf_idf_doc)

        b = avg_v / index
        # print b
        for i in range(len(vocab)):
            idf = math.log1p(float(docs_len) / float(word_doc_count[i]))
            idfs.append(idf)
            if word_doc_count[i] > 0:
                word_tf_idf_avg[i] = word_tf_idf_sum[i] / word_doc_count[i]
            else:
                word_tf_idf_avg[i] = 0
            if word_tf_idf_avg[i] > b/2 and words_count[i] > 1 and word_doc_count[i] > 1 and vocab[i] not in stop_set:
                word_important.append(vocab[i])
                # print vocab[i], word_tf_idf_avg[i], words_count[i], word_doc_count[i], idf

        print len(word_important)
        # print word_important
        # print word_tf_idf_avg[vocab.index("great")]

        out = ""
        for i in range(len(docs)):
            doc = docs[i]
            if len(doc) > 0:
                if int(labels[i]) > 3:
                    label = "pos"
                elif int(labels[i]) < 3:
                    label = "neg"
                else:
                    label = "neu"

                out += label + ":"

                for word in doc:
                    if word in word_important:
                        out += str(word_important.index(word)) + " "
                out += "\n"
        # print out

        with open(filename + ".docs", 'w') as outFile:
            outFile.write(out)

        vocab_out = ""
        for i in range(len(word_important)):
            vocab_out += str(i)+":"+word_important[i]+"\n"
        with open(filename + ".vocab", 'w') as outFile:
            outFile.write(vocab_out)


read_from_folder("sample_data/acl2015_nb_3/")
