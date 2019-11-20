from Weighting import Weighting
from Preprocessing import Preprocessing
import numpy as np
class Classification :

    def __init__(self):
        self.kelas=[]
        self.weight=Weighting()
        self.prior=[]
        self.kelas_final=[]
        self.training_data=[]
        self.training_kelas=[]
    def train(self, document, kelas):
        self.kelas = kelas
        self.weight.setDocument([Preprocessing.all_in_one_without_type(documents) for documents in document for
                                 documents in documents])
        transpose = list(map(list, zip(*self.weight.getTf())))
        hasil = {}
        for x in range(len(self.kelas)):
            if self.kelas[x] in hasil:
                sum = []
                for y in range(len(transpose[x])):
                    sum.append(hasil[self.kelas[x]][y] + transpose[x][y])
                hasil[self.kelas[x]] = sum
            else:
                hasil[self.kelas[x]] = transpose[x]
        v = len(self.weight.getFeature())
        panjang=[]

        for x in hasil:
            temp = 0
            for data in hasil[x]:
                temp += data
            panjang.append(temp)
        self.kelas_final = list(hasil.keys())
        hasil = list(hasil.values())
        for y in range (len(panjang)):
            temp=[]
            for x in hasil[y]:
                temp.append(((x+1)/(panjang[y]+v)))
            self.prior.append(temp)


    def testing(self,document,type):
        self.training_kelas = type
        self.training_data=document
        print([self.do_testing(data) for data in self.training_data])



    def do_testing(self,document):
        process = Preprocessing.all_in_one_without_type(document)
        new_type = [ type for type in process for feature in self.weight.getFeature() if type in feature]
        p = {x:self.kelas.count(x) for x in self.kelas}
        item = list(p.values())
        total = sum(p.values())
        final_p=[(p/total)for p in item]
        index =[]
        for data in new_type:
            index.append(self.weight.getFeature().index(data))
        posterior=[]
        for p in range (len(final_p)):
            temp = 0
            for x in index:
                temp = self.prior[p][x]
            posterior.append(temp*final_p[p])
        return self.kelas_final[posterior.index(max(posterior))]
