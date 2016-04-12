import math
import sys

def readfile(file):
    f = open(file, 'r')
    data = []
    for line in f:
        array_line = line.split(',')
        row = []
        for i in range (0,8):
            row.append(float(array_line[i]))
        row.append(array_line[8])
        data.append(row)
    return data

def distance(A,B):
    result = 0
    for i in range(0,8):
        result = result + (A[i]-B[i])*(A[i]-B[i])
    return math.sqrt(result)

def double_sort(k,distances,values):
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


def knearest(k,data,example):
    distances = []
    values = []
    for i in range(0,k):
        d = distance(example,data[i])
        distances.append(d)
        values.append(data[i][8])
    double_sort(k,distances,values)

    for i in range (k+1,len(data)):
        d = distance(example,data[i])
        if (d < distances[k-1]):
            distances[k-1] = d
            values[k-1] = data[i][8]
            double_sort(k,distances,values)

    #Count values
    yes = 0
    no = 0
    for i in range (0,k):
        if values[i] == 'yes\n':
            yes = yes + 1
        else:
            no = no + 1

    if yes >= no:
        return 'yes'
    else:
        return 'no'

def train_nb(data):

    #Yes data
    yes_array = []
    yes_mean = [0.0]*8
    yes_count = 0

    #no data
    no_array = []
    no_mean = [0.0]*8
    no_count = 0

    #Take the mean
    for i in range (0,len(data)):
        if data[i][8] == 'yes\n':
            yes_count = yes_count + 1
            yes_array.append(data[i])
            for j in range(0,8):
                yes_mean[j] = yes_mean[j] + data[i][j]
        else:
            no_count = no_count + 1
            no_array.append(data[i])
            for j in range(0,8):
                no_mean[j] = no_mean[j] + data[i][j]
    for j in range(0,8):
        yes_mean[j] = yes_mean[j]/yes_count
        no_mean[j] = no_mean[j]/no_count


    yes_var = [0.0]*8
    no_var = [0.0]*8
    for i in range(0,yes_count):
        for j in range(0,8):
                yes_var[j] = yes_var[j] + (yes_array[i][j]-yes_mean[j])*(yes_array[i][j]-yes_mean[j])
    for i in range(0,no_count):
        for j in range(0,8):
                no_var[j] = no_var[j] + (no_array[i][j]-no_mean[j])*(no_array[i][j]-no_mean[j])

    for j in range(0,8):
        yes_var[j] = yes_var[j]/(yes_count-1)
        no_var[j] = no_var[j]/(no_count-1)

    p_yes = float(yes_count)/(yes_count+no_count)
    p_no = float(no_count)/(yes_count+no_count)

    return [p_yes,p_no,yes_mean,yes_var,no_mean,no_var]


def normal_probability(x,mean,var):
    return (float(1)/(math.sqrt(var)*math.sqrt(2*math.pi)))*math.exp(-((x-mean)*(x-mean))/(2*var))

def naive_bayes(example,data):
    p_yes = data[0]
    p_no = data[1]
    yes_mean = data[2]
    yes_var = data[3]
    no_mean = data[4]
    no_var = data[5]

    nb_yes = 1
    nb_no = 1
    for i in range(0,8):
        nb_yes = nb_yes * normal_probability(example[0],yes_mean[0],yes_var[0])
        nb_no = nb_no * normal_probability(example[0],no_mean[0],no_var[0])
    nb_yes = nb_yes*p_yes
    nb_no = nb_no*p_no
    if nb_yes >= nb_no:
        return 'yes'
    else:
        return 'no'

file = sys.argv[1]
examples = sys.argv[2]
algorithm = sys.argv[3]
if algorithm != 'NB':
    algorithm = algorithm.replace("NN", "")


data = readfile(file)
train = train_nb(data)
f = open(examples, 'r')
for line in f:
    array_line = line.split(',')
    row = []
    for i in range (0,8):
        row.append(float(array_line[i]))
    if algorithm != 'NB':
        print knearest(int(algorithm),data,row)
    else:
        print naive_bayes(row,train)
