import math, os


def read_from_folder(folder_name):
    stop_list = []
    # with open("sample_data\stopword1.txt", "r") as stopListFile:
    #     for line in stopListFile:
    #         stop_list.append(line[:len(line) - 1])

    # print stop_list
    stop_set = set(stop_list)

    for subFolderName in os.listdir(folder_name):
        filename = folder_name + "/" + subFolderName
        convert(filename, stop_set)


def convert(filename, stop_set):
    filename = filename.replace(".txt", "")
    name = filename.split("/")[-1:][0]
    print name
    with open(filename + ".txt", "r") as txtFile:
        words = []
        docs = []
        labels = []
        word_important = []

        for line in txtFile:
            temp = line.rstrip().split("\t")
            content = temp[1].rstrip().split(" ")
            labels.append(temp[0])
            words += content[:]
            docs.append(content[:])
        word_set = set(words)
        print (len(words), len(word_set))
        vocab = []

        for word in word_set:
            if word not in stop_set:
                vocab.append(word)

        docs_out = ""
        txt_out = ""

        index = 0
        for doc in docs:
            docs_out += labels[index][-3:] + ":"
            txt_out += labels[index] + "\t"
            for word in doc:
                if word in vocab:
                    docs_out += str(vocab.index(word))+" "
                    txt_out += word+" "
            docs_out += "\n"
            txt_out += "\n"
            index += 1

        outFolder = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_100_convert/"+name

        if not os.path.exists(outFolder):
            os.makedirs(outFolder)

        with open(outFolder+"/"+name + ".docs", 'w') as outFile:
            outFile.write(docs_out)

        with open(outFolder+"/"+name + ".txt", 'w') as outFile:
            outFile.write(txt_out)

        vocab_out = ""
        index = 0
        for word in vocab:
            vocab_out += str(index)+":"+word+"\n"
            index += 1

        with open(outFolder+"/"+name + ".vocab", 'w') as outFile:
            outFile.write(vocab_out)
        # print (docs_out)


read_from_folder("G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/data/abc_100")
