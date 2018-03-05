from ..data_processing import ReadData, SelectDocument
from ..components import KnowledgeMiner, ObjectiveFunction


# folder_name = "sample_data/acl2015_nb_1/"
# rd = ReadData.ReadData()
# domains = rd.read_folder(folder_name)
# for docs in domains:
#     label_counts = [0, 0, 0]
#     length = 0
#     for doc in docs:
#         if doc.label == 'pos':
#             label_num = 0
#         elif doc.label == 'neg':
#             label_num = 1
#         else:
#             label_num = 2
#         label_counts[label_num] += 1
#         length += len(doc.words)
#     print length, label_counts

dataPath = 'sample_data/acl2015_nb'
km = KnowledgeMiner.KnowledgeMiner(dataPath)
for task in km.pis.tasks:
    of = ObjectiveFunction.ObjectiveFunction(task)
    ofs = of.calculate()
    sd = SelectDocument.SelectDocument()
    sd.select(task, ofs, "sample_data/acl2015_nb_2")
    # break
