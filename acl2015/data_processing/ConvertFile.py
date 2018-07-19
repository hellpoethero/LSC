import math, os


def read_from_folder(folder_name):
    stop_list = []
    with open("sample_data/stopword.txt", "r") as stopListFile:
        for line in stopListFile:
            stop_list.append(line[:len(line) - 1])

    # print stop_list

    outFolder = "sample_data/180709_2/"
    for subFolderName in os.listdir(folder_name):
        filename = folder_name + "/" + subFolderName
        convert(filename, stop_list, outFolder)
        # break


def convert(filename, stop_set, outFolder):
    with open(filename, "r") as txtFile:
        # txtFile.readline()
        words = []
        docs = []
        labels = []
        word_important = []
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

        count_x = []
        count_word_doc = []
        for i in range(0, 10):
            count_x.append(0)
            count_word_doc.append(0)
        words_count = []
        word_doc_count = []
        for word in vocab:
            count = words.count(word)
            words_count.append(count)
            word_doc_count.append(0)
            # print word, count
            for i in range(0, 10):
                if count > i:
                    count_x[i] += 1

        for doc in docs:
            word_doc_set = set(doc)
            for word in word_doc_set:
                word_index = vocab.index(word)
                word_doc_count[word_index] += 1

        index = 0
        for word in vocab:
            # print word, word_doc_count[index]
            for i in range(0, 10):
                if word_doc_count[index] > i:
                    count_word_doc[i] += 1
            index += 1

        print count_x
        print count_word_doc

        # print stop_set

        t_1 = 5
        t_2 = 5
        out = ''
        doc_index = 0
        for doc in docs:
            new_content = ''
            for word in doc:
                word_index = vocab.index(word)
                # print word, words_count[word_index], word_doc_count[word_index]
                if word_doc_count[word_index] >= t_2 and word not in stop_set:
                    new_content += word + ' '
            # print new_content.rstrip()
            out += labels[doc_index] + '\t' + new_content.rstrip() + '\n'
            doc_index += 1

        # print out

        name = filename.split('/')[-1]
        print name
        with open(outFolder + '/' + name, 'w') as outFile:
            outFile.write(out)

        # print len(word_important)
        # print word_important
        # print word_tf_idf_avg[vocab.index("great")]

        # out = ""
        # for i in range(len(docs)):
        #     doc = docs[i]
        #     if len(doc) > 0:
        #         if int(labels[i]) > 3:
        #             label = "pos"
        #         elif int(labels[i]) < 3:
        #             label = "neg"
        #         else:
        #             label = "neu"
        #
        #         out += label + ":"
        #
        #         for word in doc:
        #             if word in word_important:
        #                 out += str(word_important.index(word)) + " "
        #         out += "\n"
        # print out

        # with open(filename + ".docs", 'w') as outFile:
        #     outFile.write(out)
        #
        # vocab_out = ""
        # for i in range(len(word_important)):
        #     vocab_out += str(i)+":"+word_important[i]+"\n"
        # with open(filename + ".vocab", 'w') as outFile:
        #     outFile.write(vocab_out)


read_from_folder("sample_data/180709_1/")
