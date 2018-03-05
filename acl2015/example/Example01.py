from ..components import KnowledgeMiner, KnowledgeBasedLearner

dataPath = 'sample_data/acl2015_nb_3'
km = KnowledgeMiner.KnowledgeMiner(dataPath)
current_task_index = 0
km.set_current_task(current_task_index)
kbl = KnowledgeBasedLearner.KnowledgeBaseLearner(km, 1, 10, 6, 6, 0.1)
# kbl.optimize()

# filename = "G:/Hoc tap/NCKH/KT Lab/LifeLongLearning/code/LSC/sample_data/acl2015_nb_1/Baby/Baby"
# TFIDF.tf_idf(km.pis.tasks[1].docs, km.pis.tasks[1].words, filename)
