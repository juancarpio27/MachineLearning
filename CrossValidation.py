##########################################
#
# CrossValidation.py
# Juan Andres Carpio
# Naomi Serfaty
#
##########################################

import NaiveBayes
import KNN

#Function that divides de data in 10 stratified folds
#In:
#data: array with all the data
#Out:
#fold_array: array with 10 arrays, every fold produced
def fold_divide(data):
    #Create empty arrays for yes and no, usefull for stratification
    yes_array = []
    no_array = []

    #Divide the data in yes or no
    for i in range(0,len(data)):
        length = len(data[i])-1
        if (data[i][length] == 'yes'):
            yes_array.append(data[i])
        else:
            no_array.append(data[i])

    #Count how many of each section will go to every fold
    yes_fold = len(yes_array)/10
    no_fold = len(no_array)/10

    #Fold array
    folds_array = []

    #Create the 10 folds
    for i in range(0,10):
        fold = []
        #Add yes values to fold
        start_yes = i*yes_fold
        for j in range (start_yes,start_yes+yes_fold):
            fold.append(yes_array[j])
        #Add no values to fold
        start_no = i*no_fold
        for j in range (start_no,start_no+no_fold):
            fold.append(no_array[j])
        folds_array.append(fold)

    #Add the rest of the values to be sure to have only 1 more element
    #per fold if the amount of data is no divisible by 10
    j = 0
    for i in range (yes_fold*10,len(yes_array)):
        folds_array[j].append(yes_array[i])
        j = j + 1

    for i in range (no_fold*10,len(no_array)):
        folds_array[j].append(no_array[i])
        j = j + 1

    #Write in the file with the desired format
    f = open('pima-fold.csv', 'w')

    for i in range(0,10):
        f.write("fold"+str(i+1)+"\n")
        for j in range (0,len(folds_array[i])):
            for k in range (0, len(folds_array[i][j])):
                f.write(str(folds_array[i][j][k]))
                if k < len(folds_array[i][j])-1:
                    f.write(',')
            f.write("\n")
        f.write("\n")

    f.close()

    return folds_array

#Function that calculate the accuracy of a KNN algorithm using data
#In:
#k: number of neighboors
#folds_array: array with all the folds
#Out:
#accuracy: accuracy of the algorithm based on the 10 folds
def cross_validation_nn(k,folds_array):

    #Initial values
    corrects = 0
    incorrects = 0

    #Separate train and test data
    for i in range(0,10):
        training_data = []
        test_data = []
        for j in range(0,10):
            if j == i:
                test_data = folds_array[j]
            else:
                training_data = training_data + folds_array[j]
        #Predict values
        for j in range(0,len(test_data)):
            prediction = KNN.knearest(k,training_data,test_data[j],True)
            length = len(test_data[j])-1
            #Check if the value is correct
            if prediction == test_data[j][length]:
                corrects = corrects + 1
            else:
                incorrects = incorrects + 1

    return float(corrects)/float(corrects+incorrects)

#Function that calculate the accuracy of a NB algorithm using data
#In:
#folds_array: array with all the folds
#Out:
#accuracy: accuracy of the algorithm based on the 10 folds
def cross_validation_nb(folds_array):
    #Initial values
    corrects = 0
    incorrects = 0

    #Separate train and test data
    for i in range(0,10):
        training_data = []
        test_data = []
        for j in range(0,10):
            if j == i:
                test_data = folds_array[j]
            else:
                training_data = training_data + folds_array[j]

        #Train the algorithm using training data
        train = NaiveBayes.train_nb(training_data)
        #Predict values
        for j in range(0,len(test_data)):
            prediction = NaiveBayes.naive_bayes(test_data[j],train)
            length = len(test_data[j])-1
            #Check if the value is correct
            if prediction == test_data[j][length]:
                corrects = corrects + 1
            else:
                incorrects = incorrects + 1

    return float(corrects)/float(corrects+incorrects)

