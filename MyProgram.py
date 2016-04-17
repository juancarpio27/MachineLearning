##########################################
#
# MyProgram.py 
# Juan Andres Carpio
# Naomi Serfaty
#
##########################################

import sys
import NaiveBayes
import KNN
import Helper
import CrossValidation

##############################
#                            #
# Main program               #
#                            #
##############################
#Read information from the command line
file = sys.argv[1]
examples = sys.argv[2]
algorithm = sys.argv[3]

#Check with algorithm will be used
if algorithm != 'NB':
    algorithm = algorithm.replace("NN", "")

#Read data and train it for Naive Bayes
data = Helper.readfile(file)
train = NaiveBayes.train_nb(data)

#Read example data
f = open(examples, 'r')

#Test every example
for line in f:
    array_line = line.split(',')
    row = []
    length = len(array_line)
    for i in range (0,length):
        row.append(float(array_line[i]))

    #Apply the algorithm
    if algorithm != 'NB':
        print KNN.knearest(int(algorithm),data,row)
    else:
        print NaiveBayes.naive_bayes(row,train)


##############################
#                            #
# Cross validation called    #
# when need it               #
#                            #
##############################
#folds = CrossValidation.fold_divide(data)
#print CrossValidation.cross_validation_nn(1,folds)
#print CrossValidation.cross_validation_nb(folds)


