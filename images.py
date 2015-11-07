from operator import itemgetter, attrgetter

class imageArray:
    def __init__(self, pic):
        #Turn into dictionary of the form (word category, list of words within that category)
        file = open("trainingimages", 'r')
        for line in file:
            print ('1')
            
           