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

#Function to read data from a text file
#In: 
#file: name of the text file with the data
#Out:
#data: matrix where every row correspond to a line of data from file
def readfile(file):
    f = open(file, 'r')
    data = []
    for line in f:
        line = line.replace("\r\n","")
        array_line = line.split(',')
        row = []
        for i in range (0,8):
            row.append(float(array_line[i]))
        row.append(array_line[8])
        data.append(row)
    return data

##############################
#                            #
# Main program               #
#                            #
##############################
#Read information from the command line
file = sys.argv[1]
examples = sys.argv[2]
algorithm = sys.argv[3]
#Check with algorithm
if algorithm != 'NB':
    algorithm = algorithm.replace("NN", "")

#Read data and train it for Naive Bayes
data = readfile(file)
train = NaiveBayes.train_nb(data)

#Read example data
f = open(examples, 'r')

#Test every example
for line in f:
    array_line = line.split(',')
    row = []
    for i in range (0,8):
        row.append(float(array_line[i]))

    #Apply the algorithm
    if algorithm != 'NB':
        print KNN.knearest(int(algorithm),data,row)
    else:
        print NaiveBayes.naive_bayes(row,train)


