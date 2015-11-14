from math import *
from operator import itemgetter, attrgetter                                                           

class NumberClass:
    def __init__(self):
        #Turn into dictionary of the form (word category, list of words within that category
        self.Feature = []
        self.count = 0
        self.MAP = 0
        for i in range(784):
            self.Feature.append(0)
        
    def addToFeature(self,adder, positiony, positionx):
        self.Feature[positionx+positiony*28] += adder
        
    def addToCount(self, adder):
        self.count += adder
    
    def getFeature (self, positiony, positionx):
        FeatureValue = self.Feature[positionx+28*positiony]
        return FeatureValue

    def getCount(self):
        countValue = self.count
        return countValue
    
    def getMAP(self, number):
        self.MAP += log10(float(self.count)/number)
        for row in range(28):
            for column in range(28):
                value = float(self.Feature[column+28*row])/self.count
                self.MAP += log10(value)
        return self.MAP