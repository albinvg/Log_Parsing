path = "C:\\Users\\"+"\\LogParsing.txt"

#read content of a file into List using "readlines"
with open(path, 'r') as f:
    File = f.readlines()

#split each line into a list. Thus making it a list of lists
for i in range(len(File)):
    File[i] = File[i].split(',')
    File[i][3] = File[i][3][:-1]

#create a function that takes the listofLists as input, along with the column that needs to be sorted
def FnSort(lst, n):
    for i in range(2, len(lst)):

        while i > 1:
            if int(lst[i][n]) < int(lst[i-1][n]):
                temp = lst[i]
                lst[i] = lst[i-1]
                lst[i - 1] = temp
            i -= 1
    return (lst[:-6:-1])        #it will return the rows with the largest 5 values in the sorted column


FnSort(File, 3)
