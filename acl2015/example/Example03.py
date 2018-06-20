from ..components import CloseDomain
import numpy as np

close_domain_path = 'sample_data/stat/1523723936697'
close_domain = CloseDomain.CloseDomain(close_domain_path)
close_domain.read_folder()

arr = np.array([1, 3, 2, 4, 5])
a = np.argsort(arr)
# print a[::-1]
