from operator import itemgetter, attrgetter                                                           

class imageArray:
    def __init__(self, fileNameTraining, fileNameTesting):
        #Turn into dictionary of the form (word category, list of words within that category)
        file = open(fileNameTraining, 'r')
        file2 = open(fileNameTesting, 'r')
        self.labelList = []
        self.imageList = []
        image = []
        j = 0
        i = 0
        lineNum = 0
        for line in file:
            image.append(line)
            j += 1
            lineNum += 1
            if j > 27:
                j = 0
                i += 1
                #print image
                self.imageList.append(image)
                image = []
        for line in file2:
            self.labelList.append(line)
        #print len(self.imageList)
    def getImage(self,position):
        image = []
        image = self.imageList[position]
        return image
        
    def getLabels(self, position):
        label = self.labelList[position]
        return label
           