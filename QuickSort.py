path = "C:\\Users\\aasdasd"+"\\LogParsing.txt"

with open(path, 'r') as f:
    array = f.readlines()
    header = array.pop(0)

for i in range(len(array)):
    array[i] = array[i].split(',')
    array[i][3] = array[i][3][:-1]

def fnQuickSort(array):
    if len(array) <= 1:
        return (array)
    else:
        pivot = array.pop()
        smallerList = []
        largerList = []

        for i in range(len(array)):
            if int(array[i][3]) < int(pivot[3]):
                smallerList.append(array[i])
            else:
                largerList.append(array[i])
        return fnQuickSort(smallerList) + [pivot] + fnQuickSort(largerList)


print(fnQuickSort(array)[-5:])
