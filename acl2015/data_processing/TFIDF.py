import math


def tf_idf(docs, vocabs, filename):
    word_doc_count = []
    words_count = []
    word_tfidf_sum = []
    word_tfidf_avg = []
    docs_len = len(docs)
    for word in vocabs:
        word_doc_count.append(0)
        word_tfidf_sum.append(0)
        word_tfidf_avg.append(0)
        words_count.append(0)
    print len(vocabs), docs_len
    for doc in docs:
        word_set = set(doc.words)
        for word in word_set:
            word_doc_count[int(word)] += 1
            words_count[int(word)] += doc.words.count(word)

    tf_idf_matrix = []

    avg_v = 0
    avg_v_1 = 0
    max_v = 0
    min_v = 0
    index = 0
    index_1 = 0
    for doc in docs:
        words = doc.words
        word_set = set(words)
        doc_len = len(words)
        tf_idf_doc = []
        for word in word_set:
            word_count = words.count(word)
            tf = float(word_count) / float(doc_len)
            a = tf * math.log1p(docs_len / word_doc_count[int(word)])
            avg_v += a
            index += 1
            if a > 0:
                avg_v_1 += a
                index_1 += 1
            if a > max_v:
                max_v = a
            if a < min_v:
                min_v = a
            # print vocabs[int(word)], a
            word_tfidf_sum[int(word)] += a
            tf_idf_doc.append(a)
        # print "----------"
            tf_idf_matrix.append(tf_idf_doc)

    word_important = []
    b = avg_v / index
    for i in range(len(vocabs)):
        if word_doc_count[i] > 0:
            word_tfidf_avg[i] = word_tfidf_sum[i] / word_doc_count[i]
        else:
            word_tfidf_avg[i] = 0
        if word_tfidf_avg[i] > b and words_count[i] > 1:
            word_important.append(str(i))
            # print vocabs[i], word_tfidf_avg[i], words_count[i]

    out = ""
    for doc in docs:
        out += doc.label+"\t"
        a_set = set(word_important)
        for word in doc.words:
            if word in a_set:
                out += word+" "
        out += "\n"
    # print out

    # filename = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb/Baby/Baby"
    with open(filename + ".docsxx", 'w') as outFile:
        outFile.write(out)

    print avg_v / index, avg_v_1 / index_1, max_v, min_v, len(word_important)
    pass



