from ..components import Model

folder = 'G:/Hoc tap/NCKH\KT Lab/LifeLongLearning/model/'
subFolder = '/180709_2_100_split_1531129463854/'
filename = folder + subFolder + '/AlarmClock_0.nb.model'
model = Model.Model(filename)

true_pos = 0
true_neg = 0
false_pos = 0
false_neg = 0
testFilename = 'sample_data/180709_2_100_split/AlarmClock/AlarmClock_test_0.txt'
with open(testFilename, 'r') as testFile:
    for line in testFile:
        label = line.split('\t')[0]
        content = line.split('\t')[1]
        predicted_label = model.predict_label(content)
        if predicted_label == label:
            if predicted_label == '__label__pos':
                true_pos += 1
            else:
                true_neg += 1
        else:
            if predicted_label == '__label__pos':
                false_pos += 1
            else:
                false_neg += 1
# print true_pos, true_neg, false_pos, false_neg
p_pos = float(true_pos)/float(true_pos + false_pos)
r_pos = float(true_pos)/float(true_pos + false_neg)
p_neg = float(true_neg)/float(true_neg + false_neg)
r_neg = float(true_neg)/float(true_neg + false_pos)
a = float(true_neg + true_pos)/(true_pos + true_neg + false_pos + false_neg)

# print p_pos, r_pos, 2 * p_pos * r_pos / (p_pos + r_pos)
# print p_neg, r_neg, 2 * p_neg * r_neg / (p_neg + r_neg)
print a
