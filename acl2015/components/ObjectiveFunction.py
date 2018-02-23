class ObjectiveFunction:
    def __init__(self):
        pass

    def calculate(self, doc):
        for w in doc:
            print(w)
        print doc.label
        pass


o = ObjectiveFunction()
