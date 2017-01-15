from math import log

'''
 Shannon entrophy
   - Sum(i = 1 to N) of p(x sub i) log2 p(x sub i)
   where p(x) is the probability of choosing this class
'''

def calcShannonEnt(dataSet):
  # Number of entries in the dataset
  numEntries = len(dataSet)
  labelCounts = {}
  # Creates a dictionary whose keys are the values in the
  # final column
  for featVect in dataSet:
    currentLabel = featVect[-1]
    # if the label is not here we add it
    if currentLabel not in labelCounts.keys():
      labelCounts[currentLabel] = 0
    else:
    # else we keep the number of occurences
      labelCounts[currentLabel] += 1
  shannonEnt = 0.0
  for key in labelCounts:
    prob = float(labelCounts[key]) / numEntries
    try:
      shannonEnt -= prob * log(prob,2)
      break
    except ValueError:
      shannonEnt = 0
  return shannonEnt

# Set up our dataset
# columns are: Can survive w/o coming to surface?, has flippers?, Fish?
def createDataSet():
  dataSet = [[1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]
  labels = ['no surfacing','flippers']
  return dataSet, labels


# dataSet = the dataset that we want to split
# axis = the feature that we want to split based on
# value the value that we wanna use to get the splits
def splitDataSet(dataSet, axis, value):
  # create separate list
  retDataSet = []
  # cut out the feature split on
  for featVect in dataSet:
    if featVect[axis] == value:
      reducedFeatVect = featVect[:axis]
      # [1,2,3].add([4,5,6]) = [1,2,3, [4,5,6]] and [1,2,3].extend([4,5,6]) = [1,2,3,4,5,6]
      reducedFeatVect.extend(featVect[axis+1:])
      retDataSet.append(reducedFeatVect)
  return retDataSet

# e.g. in our dataset where [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
# calling splitDataSet w/ splitDataSet(myDat,0,1) will return [[1, 'yes'], [1, 'yes'], [0, 'no']]
# bc it grabs all the vectors that has a 1 on the 0 component

def chooseBestFeatureToSplit(dataSet):
    # Makin assumptions about the data, like it's a list of list
    # square and last column are the labels
    numFeatures = len(dataSet[0]) - 1
    # We calculate the entropy for the whole set
    # to get the base disorder
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        # Create unique list of class labels
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # Calculate entropy for each split
            subDataSet = splitDataSet(dataSet, i , value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy + newEntropy
        # Find the best information gain
        if (infoGain > bestInfoGain):
          bestInfoGain = infoGain
          bestFeature = i
    return bestFeature

# This function takes a list of classnames
# and then creates a dictionary whose keys
# are the unique values in classList and the object
# is the frequency of occurence in each class label of classList
# then it sorts by the keys and returns the class that occurs with the
# greatest frequency
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classList.keys() : classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
      key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # Stop when all classes are equal
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # When not more features reutnr majority
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    # get the list of unique values
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet\
                           (dataSet, bestFeat, value), subLabels)
    return myTree


def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
      if testVec[featIndex] == key:
        if type(secondDict[key]).__name__ == 'dict'
          classLabel = classify(secondDict[key], featLabels, testVec)
        else:
          classLabel = secondDict[key]
   return classLabel
