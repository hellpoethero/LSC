from ..components import KnowledgeMiner, KnowledgeBasedLearner, TargetTask

dataPath = 'sample_data/acl2015_nb_4'
km = KnowledgeMiner.KnowledgeMiner(dataPath)
current_task_index = 0
km.set_current_task(current_task_index)

target = TargetTask.TargetTask(km.get_current_task(), 5)
# target.get_test_data()
target.get_train_data()

for doc in target.docs:
    print doc.words
print "--------------------------"
for doc in target.get_train_data()[0].docs:
    print doc.words
print "--------------------------"
for doc in target.get_test_data()[0]:
    print doc.words

# kbl = KnowledgeBasedLearner.KnowledgeBaseLearner(target.get_train_data()[0], km, 1, 10, 6, 6, 0.1)
# kbl.optimize()

true_pos = 0
true_neg = 0
false_pos = 0
false_neg = 0
#
# for i in range(0, 5):
#     kbl_1 = KnowledgeBasedLearner.KnowledgeBaseLearner(target.get_train_data()[i], km, 1, 10, 6, 6, 0.1)
#     docs = target.get_test_data()[i]
#     for doc in docs:
#         # print doc.words
#         sentence = ""
#         for word in doc.words:
#             sentence += target.words[int(word)]+" "
#         # print sentence
#         label = kbl.calculate_label(sentence)
#         # print doc.label
#         # print "----------"
#
#         if label == 'pos':
#             if label == doc.label:
#                 true_pos += 1
#             else:
#                 false_pos += 1
#         else:
#             if label == doc.label:
#                 true_neg += 1
#             else:
#                 false_neg += 1
#
# print true_pos, true_neg, false_pos, false_neg

# filename = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb_1/Baby/Baby"
# TFIDF.tf_idf(km.pis.tasks[1].docs, km.pis.tasks[1].words, filename)
#
# fileName = "sample_data/acl2015_nb_3/AlarmClock/AlarmClock.txt"
# with open(fileName, 'r') as inputFile:
#     inputFile.readline()
#     for line in inputFile:
#         doc = line.split("\t")[1].rstrip().lower()
#         print doc
#         print line.split("\t")[0].rstrip()
#         kbl.calculate_label(doc)
#         print "----------"

# sentence = "observation timexlicensed product consist independent analog clock AMFM clock radio digital display show either time tuner s frequency note digital tuner display digital tuner clock plug lrb via include power adapter rrb analog clock face digital display light time two brightness setting run battery power light though can get brief pulse light hit snooze bar tiny luminescent bar analog clock s hand pro decent sound cheap clock radio lrb expect bass rrb decent fm reception exactly lightweight work battery probably wellsuited car camping amber clock lighting lrb time unit plug rrb okay digital frequency readout improvement typical cheap analog tuner con number user interface problem example oftused switch radio offon hide side seldomused button like time set prominent annoy synchronize separate analog digital clock clock lighting battery mode except briefly hit snooze bar BUT sleep timer hit bar will also cancel sleep mode turn radio nature sound run battery way light clock without cause undesirable sideeffect radio frequency display helpful digital time readout radio I find frequency display jitter lot radio station lrb eg tune jump around everything inbetween rrb audio sound fine visual annoyance tuning dial sensitive require fair amount concentration fine motor control tune specific frequency overall tuner better cheap analog worse cheap digital one last thing clock face fold travel position muffle radio speaker open position angle clock face adjustible lrb see photo vertical get rrb bottom line I return less job design lack intelligence must something better ";
# sentence = sentence.lower()
# print sentence
# kbl.calculate_label(sentence)
