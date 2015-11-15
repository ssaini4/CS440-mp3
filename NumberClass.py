from math import *
import numpy as np
from operator import itemgetter, attrgetter                                                           

class NumberClass:
    def __init__(self):
        #Turn into dictionary of the form (word category, list of words within that category
        self.Feature = []
        self.likelihoods1 = []
        self.likelihoods0 = []
        self.count = 0
        self.MAP = 0
        for i in range(784):
            self.Feature.append(0)
            self.likelihoods1.append(0)
            self.likelihoods0.append(0)
        
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
        print "Counts", self.count
        self.MAP += np.log(float(self.count)/number)
        for row in range(28):
            for column in range(28):
                value = float(self.Feature[column+28*row])/self.count
                self.MAP += np.log(value)
                self.likelihoods1[row*28+column] = np.log(value)
                self.likelihoods0[row*28+column] = np.log10(1-value)
        return self.MAP
    
    def getTestScore(self, featureVector):
        score = np.log(float(self.count)/5000)
        for row in range(28):
            for column in range(28):
                if featureVector[row*28+column] != 0:
                    score += self.likelihoods1[row*28+column]
                else:
                    score += self.likelihoods0[row+28*column]
        return score