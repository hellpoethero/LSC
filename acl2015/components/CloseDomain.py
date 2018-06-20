import os
import numpy as np


class CloseDomain:
    def __init__(self, path):
        self.path = path
        self.v = []
        self.w = []
        self.t = []
        self.v_sort = []
        self.w_sort = []
        self.t_sort = []
        pass

    def read_folder(self):
        for filename in os.listdir(self.path):
            filename = self.path + "/" + filename
            self.read_file(filename)

    def read_file(self, filename):
        v_domain = []
        w_domain = []
        t_domain = []
        with open(filename, 'r') as close_domain_file:
            close_domain_file.readline()
            for line in close_domain_file:
                value = line.rstrip().split(',')
                v_domain.append(value[3])
                w_domain.append(value[4])
                t_domain.append(value[8])

                # print [value[3], value[4], value[8]]

        self.v.append(v_domain)
        self.w.append(w_domain)
        self.t.append(t_domain)

        self.v_sort.append(np.argsort(np.array(v_domain))[::-1])
        self.w_sort.append(np.argsort(np.array(w_domain))[::-1])
        self.t_sort.append(np.argsort(np.array(t_domain))[::-1])
