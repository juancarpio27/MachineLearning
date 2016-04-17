##########################################
#
# KNN.py
# Juan Andres Carpio
# Naomi Serfaty
#
##########################################


import math

#Function that calculates the Eucledian distance between two points
#In:
#A: first array
#B: second array
#Out:
#Eucledian distance between them
def distance(A,B,named=False):
    result = 0.0
    if named:
        for i in range(0,len(A)-1):
            result = result + ((A[i]-B[i])*(A[i]-B[i]))
    else:
        for i in range(0,len(A)):
            result = result + ((A[i]-B[i])*(A[i]-B[i]))
    return math.sqrt(result)

#Function that sort the array of distances,
# keeping the array of values with the same order
#using the algorithm of bubble sort
def double_sort(k,distances,values):
    #Bubblesort algorithm
    for j in range (0,k-1):
        min = j
        for i in range (j+1,k):
            if distances[i] < distances[min]:
                min = i

        #swap min and j
        temp_d = distances[min]
        temp_v = values[min]
        distances[min] = distances[j]
        values[min] = values[j]
        distances[j] = temp_d
        values[j] = temp_v

#Function that predict the value for an example using K nearest neighbour algorithm
#In:
#example: value to classify
#data: data to use for the classification
#k: number of neighbours
#Out:
#classification result: yes or no
def knearest(k,data,example,named=False):

    #Initiate values
    distances = []
    values = []

    #First k values
    for i in range(0,k):
        d = distance(example,data[i],named)
        distances.append(d)
        length = len(data[i])-1
        values.append(data[i][length])
    double_sort(k,distances,values)

    #For each value calculate the distance. If it is less than the
    #maximun stored value, switch them and sort the array of neighbours
    for i in range (k+1,len(data)):
        d = distance(example,data[i],named)
        if (d <= distances[k-1]):
            distances[k-1] = d
            length = len(data[i])-1
            values[k-1] = data[i][length]
            double_sort(k,distances,values)

    #Count values
    yes = 0
    no = 0
    for i in range (0,k):
        if values[i] == 'yes':
            yes = yes + 1
        else:
            no = no + 1

    #Classification
    if yes >= no:
        return 'yes'
    if yes < no:
        return 'no'