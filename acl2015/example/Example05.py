import os
from ..components import Model

folder = 'G:/Hoc tap/NCKH\KT Lab/LifeLongLearning/model/'
subFolder = '180709_2_100_split_1531277168350_lsc_close'
testFolder = 'sample_data/180709_2_100_split/'

acc = []
acc_v = []
counts = []
names = []

index = 0
for filename in os.listdir(folder + subFolder):
    modelName = folder + subFolder + '/' + filename
    # print modelName
    domain = modelName.split('/')[-1].split('.')[0][:-2]
    testFilename = testFolder + domain + '/' + domain + '_test_' + str(index % 5) + '.txt'
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

    # print p_pos, r_pos, 2 * p_pos * r_pos / (p_pos + r_pos)
    # print p_neg, r_neg, 2 * p_neg * r_neg / (p_neg + r_neg)
    print domain, index % 5, a
    acc.append(a)
    counts.append([true_pos, true_neg, false_pos, false_neg])
    if index % 5 == 0:
        names.append(domain)
    index += 1

c = []
i = 0
for count in counts:
    if i % 5 == 0:
        c.append(count)
    else:
        j = 0
        for v in count:
            c[i/5][j] += v
            j += 1
    i += 1

t = 0.0
at = 0.0
index = 0
for a in acc:
    t += a
    at += a
    if index % 5 == 4:
        acc_v.append(t/5)
        t = 0.0
    index += 1

# print at / index
print c
outFolder = '../../result/'
i = 0
with open(outFolder + subFolder + '.csv', 'w') as outFile:
    outFile.write('Domain;P pos;R pos;F1 pos;P neg;R neg;F1 neg;A;\n')
    for value in c:
        # for v in value:
        #     outFile.write(str(v) + ';')

        p_pos = float(value[0]) / float(value[0] + value[2])
        r_pos = float(value[0]) / float(value[0] + value[3])
        p_neg = float(value[1]) / float(value[1] + value[3])
        r_neg = float(value[1]) / float(value[1] + value[2])
        p_f1 = 2 * p_pos * r_pos / (p_pos + r_pos)
        f_f1 = 2 * p_neg * r_neg / (p_neg + r_neg)
        a = float(value[0] + value[1]) / (value[0] + value[1] + value[2] + value[3])
        outFile.write(names[i] + ';')
        outFile.write(str(p_pos) + ';' + str(r_pos) + ';' + str(p_f1) + ';')
        outFile.write(str(p_neg) + ';' + str(r_neg) + ';' + str(f_f1) + ';')
        outFile.write(str(a))
        outFile.write('\n')
        i += 1
    outFile.write(';;;;;;;' + str(at / index))
    outFile.close()
