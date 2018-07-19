import os
from ..components import Model

folder = 'G:/Hoc tap/NCKH\KT Lab/LifeLongLearning/model/'
subFolder = '180709_2_100_split_1531231333649_nb_close'
testFolder = 'sample_data/180709_2_100/'

acc = []
acc_v = []

for filename in os.listdir(folder + subFolder):
    modelName = folder + subFolder + '/' + filename
    # print modelName
    domain = modelName.split('/')[-1].split('.')[0]
    testFilename = testFolder + domain + '.txt'
    # print domain
    model = Model.Model(modelName)

    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0
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

    f1_pos = 2 * p_pos * r_pos / (p_pos + r_pos)
    f1_neg = 2 * p_neg * r_neg / (p_neg + r_neg)
    print domain, a
    acc.append(a)
    acc_v.append([domain, str(p_pos), str(r_pos), str(f1_pos), str(p_neg), str(r_neg), str(f1_neg), str(a)])

at = 0.0
index = 0
for a in acc:
    at += a
    index += 1

print at / index

outFolder = '../../result/'
with open(outFolder + subFolder + '.csv', 'w') as outFile:
    outFile.write('Domain;P pos;R pos;F1 pos;P neg;R neg;F1 neg;A;\n')
    for value in acc_v:
        for v in value:
            outFile.write(v + ';')
        outFile.write('\n')
    outFile.write(';;;;;;;' + str(at / index))
    outFile.close()
