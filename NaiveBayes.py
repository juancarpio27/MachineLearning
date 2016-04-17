##########################################
#
# NaiveBayes.py
# Juan Andres Carpio
# Naomi Serfaty
#
##########################################

import math

#Function to train the data to use for naive bayes algorithm
#In:
#data: array with the data
#Out:
#Array with the conditional probabilty for each attribute
#for yes and no case, and probability of yes and no
def train_nb(data):
    #Initialize yes values

    length = len(data[0])-1

    yes_array = []
    yes_mean = [0.0]*length
    yes_count = 0

    #Initialize no values
    no_array = []
    no_mean = [0.0]*length
    no_count = 0

    #Get the sum of every example and many of them are
    for i in range (0,len(data)):
        if data[i][length] == 'yes':
            yes_count = yes_count + 1
            yes_array.append(data[i])
            for j in range(0,length):
                yes_mean[j] = yes_mean[j] + data[i][j]
        else:
            no_count = no_count + 1
            no_array.append(data[i])
            for j in range(0,length):
                no_mean[j] = no_mean[j] + data[i][j]

    #Divide the sum of every field by the amount of respectives examples
    #to get the mean
    for j in range(0,length):
        yes_mean[j] = yes_mean[j]/yes_count
        no_mean[j] = no_mean[j]/no_count

    #Initialize variance arrays
    yes_var = [0.0]*length
    no_var = [0.0]*length

    #For every example substract the media and elevate it two the potence of two
    for i in range(0,yes_count):
        for j in range(0,length):
            yes_var[j] = yes_var[j] + (yes_array[i][j]-yes_mean[j])*(yes_array[i][j]-yes_mean[j])
    for i in range(0,no_count):
        for j in range(0,length):
            no_var[j] = no_var[j] + (no_array[i][j]-no_mean[j])*(no_array[i][j]-no_mean[j])

    #Divide it by the amount of elements
    for j in range(0,length):
        yes_var[j] = yes_var[j]/(yes_count-1)
        no_var[j] = no_var[j]/(no_count-1)

    #Obtain the probability of yes and now
    p_yes = float(yes_count)/(yes_count+no_count)
    p_no = float(no_count)/(yes_count+no_count)

    #Return the array with all the information
    return [p_yes,p_no,yes_mean,yes_var,no_mean,no_var]

#Function to calculate the probability of a point
# based on normal distribution
#In:
#x: value to calculate
#mean: mean of the distribution
#var: variance of the distribution
#Out:
#The value of the probability of x with media and variance
def normal_probability(x,mean,var):
    return (float(1)/(math.sqrt(2*math.pi*var)))*math.exp(-((x-mean)*(x-mean)/(2*var)))

#Function that predict the value for an example using naive bayes algorithm
#In:
#example: value to classify
#data: trained data of the algorithm
#Out:
#classification result: yes or no
def naive_bayes(example,data):
    #Initiate important variables
    p_yes = data[0]
    p_no = data[1]
    yes_mean = data[2]
    yes_var = data[3]
    no_mean = data[4]
    no_var = data[5]

    #Initiate probabilities in one
    nb_yes = 1
    nb_no = 1

    length = len(yes_mean)-1

    #Caluclate each condition probabilities
    for i in range(0,length):
        nb_yes = nb_yes * normal_probability(example[i],yes_mean[i],yes_var[i])
        nb_no = nb_no * normal_probability(example[i],no_mean[i],no_var[i])

    #Product between acumulated prob and prob of each class
    nb_yes = nb_yes*p_yes
    nb_no = nb_no*p_no

    #Comparation and return
    if nb_yes >= nb_no:
        return 'yes'
    else:
        return 'no'