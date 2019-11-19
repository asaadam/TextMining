import numpy as np
import collections
class Weighting:

    def __init__(self):
        self.text = []

    def setDocument(self, document):
        self.text = document

    def getFeature(self):
        return list(collections.OrderedDict([(word, None) for document in self.text for word in document]))

    def getTf(self):
        # for feature in self.getFeature():
        #     for document in self.text:
        #         print(document.count(feature))
        return np.asarray([[document.count(feature) for document in self.text] for feature in self.getFeature()])

    def get_raw_tf(self):
        for feature in self.getFeature():
            for document in self.text:
                print(document,feature)

    def printDocument(self):
      print(self.text)
