def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', \
                    'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', \
                    'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', \
                    'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
                    'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1] # 1 is abusive 0 is not
    # returns the postingLiswt and an array of labels
    return postingList, classVec

# Creates a List of all the uniq words in all our documents
def createVocabList(dataSet):
    # creates an empty set, in python this will return an unique list
    vocabSet = set([])
    for document in dataSet:
        # append this set w/ a new set for e/ document
        # | it's used for union of 2 sets
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# This function takes a document and a vocabulary list
# and returns an array of 0's and 1's to show if a word
# of the vocab it's present on the document
def setOfWords2Vect(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word %s is not on my vocabulary" % word
    return returnVec
