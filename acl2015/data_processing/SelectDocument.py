import os
from random import shuffle


class SelectDocument:
    def __init__(self):
        pass

    @staticmethod
    def select(task, ofs, folder):
        pos = []
        neg = []
        i = 0
        for doc in task.docs:
            if doc.label == 'pos':
                pos.append(ofs[i])
            else:
                neg.append(ofs[i])
            i += 1
        pos.sort()
        neg.sort()
        pos.reverse()
        neg.reverse()
        print task.name
        print pos[100]
        print neg[100]
        i = 0
        out = "title\n"
        for doc in task.docs:
            if doc.label == 'pos':
                if ofs[i] > pos[100]:
                    out += "5\t"
                    for word in doc.words:
                        out += task.words[int(word)]+" "
                    out += "\n"
            else:
                if ofs[i] > neg[100]:
                    out += "1\t"
                    for word in doc.words:
                        out += task.words[int(word)]+" "
                    out += "\n"
            i += 1

        filename = folder+"/"+task.name+"/"+task.name+".txt"
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, "w") as outFile:
            outFile.write(out)

    @staticmethod
    def select_random(task, folder):
        shuffle(task.docs)

        pos = []
        neg = []
        for doc in task.docs:
            if doc.label == 'pos' and len(pos) < 100:
                pos.append(doc)
            elif doc.label == 'neg' and len(neg) < 100:
                neg.append(doc)
        print task.name
        i = 0
        out = ""
        docs = pos + neg
        shuffle(docs)
        for doc in docs:
            if doc.label == 'pos':
                out += "__label__pos\t"
                for word in doc.words:
                    out += task.words[int(word)] + " "
                out += "\n"
            else:
                out += "__label__neg\t"
                for word in doc.words:
                    out += task.words[int(word)] + " "
                out += "\n"
            i += 1

        filename = folder + "/" + task.name + ".txt"
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, "w") as outFile:
            outFile.write(out)
