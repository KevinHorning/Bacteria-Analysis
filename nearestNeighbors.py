# uses k-nearest neighbors algorithm to find the most similar
# bacteria sample in training data to the input bacteria sample

import csv
import math
import random

# reads vectors of training bacteria images to get 'neighbors' 
with open('D:/Coding/Python/FundDataSci/Bacteria/trainingVectors.csv') as infile:
    reader = csv.reader(infile)    
    neighborVectors = []
    for row in reader:
        vector = []
        for cell in row:
            vector.append(int(cell))
        neighborVectors.append(vector)

# k-nearest neighbor algorithm for finding most similar bacteria sample vector
# to input bacteria sample
def findNearestNeighbor(newVector): 
    if len(newVector) != len(neighborVectors[0]):
        return "Invalid length input"
    
    # calculates distances of the input vector to neighbor vectors
    distances = []
    for vector in neighborVectors:
        diffsSquared = []
        for i in range(len(vector)):
            diffsSquared.append(abs(vector[i] - newVector[i]) ** 2)
    
        total = 0
        for i in diffsSquared:
            total += i    
        distances.append(math.sqrt(total))
     
    # determines neighbor with lowest distance and returns the vector's index + 1    
    minDist = 99999
    for i in range(len(distances)):
        if distances[i] < minDist:
            minDist = distances[i]
            mindex = i
    return mindex + 1       


# tests function with vector input of random values

indices = []    
for i in range(10):
    '''
    vect = []    
    for i in range(784):
        vect.append(random.randint(0, 256))
    '''
    indices.append(trainingIndex)
print(indices)
