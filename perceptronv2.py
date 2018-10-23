# -*- coding: utf-8 -*-
"""
Perceptron Script	

activation = sum(weight_i * x_i) + bias 
bias = weights [0]
 	
prediction = 1.0 if activation > 0.0 else 0.0

This is the treshold activation

"""

# Make a prediction with weights. If the weights are wrong the prediction will be wrong.
def predict(Row, weights):
    activation = weights[0]
    for i in range(numColumns):
        activation += weights[i + 1] * dataset[Row][i]
# This is threshold activation         
    return 1.0 if activation > 0.0 else 0.0
 
#dataset can be set to anything or read from file
dataset = [[0.1, 0.9],
[0.2, 0.8],
[0.3, 0.75],
[0.5, 0.75],
[0.7, 0.65],
[0.8, 0.6],
[0.9, 0.7],
[0.1, 0.05],
[0.2, 0.1],
[0.3, 0.15],
[0.4, 0.2],
[0.5, 0.3],
[0.6, 0.55]]
#output can be set to anything or read from file but should be be equal to the number of rows of teh dataset
output = [1,1,1,1,1,1,1,0,0,0,0,0,0,0]
#weights can be set to anything to start but needs to have one more column then the dataset
#as the treshold actication either gives a zero or one as output the mean is 0.5 so setting the weights at 0.5 may be better than setting them to zero 
weights = [.5, .5, 0.5]
#this returns the number of rows in the dataset
numRows = len(dataset)
#this returns the number of columns in the dataset
numColumns= len(dataset[0])
#this calls the predict function for each of the rows to get the prediction according to the weights
for Row in range(numRows):
    prediction = predict(Row, weights)
    print("Expected=%d, Predicted=%d" % (output[Row], prediction))