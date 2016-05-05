##########################################
#
# Helper.py
# Juan Andres Carpio
# Naomi Serfaty
#
##########################################

#Function to read data from a text file
#In:
#file: name of the text file with the data
#Out:
#data: matrix where every row correspond to a line of data from file
def readfile(file):
    f = open(file, 'r')
    data = []
    for line in f:
        #TODO Change it to windows format
        line = line.replace("\r\n","")
        array_line = line.split(',')
        row = []
        length = len(array_line)-1
        for i in range (0,length):
            row.append(float(array_line[i]))
        row.append(array_line[length])
        data.append(row)
    return data

