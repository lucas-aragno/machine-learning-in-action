from numpy import *
import operator

def createDataSet():
  group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
  labels = ['A', 'A', 'B', 'B']
  return group, labels


'''
  For every point in our dataset:
    calculate the distance between inX and the current point
    sort the distances in increasing order
    take k items with lowest distances to inX
    find the majority class among these items
    return the majority class as our prediction for the class of inX
'''

def classify0(inX, dataSet, labels, k):
  dataSetSize = dataSet.shape[0]
  # Begin distance calculation
  diffMat = tile(inX, (dataSetSize, 1)) - dataSet
  sqDiffMat = diffMat**2
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances**0.5
  sortedDistIndicies = distances.argsort()
  # End distance calculation
  classCount = {}
  for i in range(k):
    # Voting w/ lowest k distances
    voteILabel = labels[sortedDistIndicies[i]]
    classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
  # Sort dictionary
  sortedClassCount = sorted(classCount.iteritems(),
    key=operator.itemgetter(1), reverse=True)
  return sortedClassCount[0][0]


# classify0 takes 4 inputs, the input vector to classify called inX
# dataSet which is our full matrix of training data
# a vector of labels called... labels...
# and k which is the number of nearest neighbors to use in the voting

# we calculate the distance using the Euclidian Distance where
# the distance between 2 vectors xA and xB, w/ 2 elements is given by

# d = sqrt( (xA[0] - xB[0])**2 + (xA[1] - xB[1])**2 )

# so... for (0,0) and (1,2)

# d = sqrt( (1 - 0)**2 + (2, 0)**2 )

# if we are working w/ 4 features like (1,0,0,1) and (7,6,9,4)

# d = sqrt( (7 - 1)**2 + (6 - 0)**2 + (9 - 0)**2 + (4 - 1)**2 )

# Finally we can call this thing by doing kNN.clasify0([0,0], group, labels, 3) where group and labels
# Are the outputs of createDataSet

