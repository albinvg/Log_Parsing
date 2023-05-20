"""
replace the value with 20% less than its current value


the cost of a meal is $27.55 and it is tasty
the cost of a meal is $37.55 and it is tasty
the cost of a meal is $47.55 and it is tasty
the cost of a meal is $527.55 and it is tasty
the cost of a meal is $267.55 and it is tasty
the cost of a meal is $277.55 and it is tasty
"""


path1 = "C:\\Users\\Elizabeth\\Desktop\\Albin\\programming\\Input.txt"
path2 = "C:\\Users\\Elizabeth\\Desktop\\Albin\\programming\\Output.txt"

with open(path1, 'r+') as file1:
    list1 = file1.readlines()

list2 = [[] for i in range(len(list1))]

for i in range(len(list1)):
    list2[i] = list1[i].split()
    list2[i][6] = '$' + str(float(list2[i][6][1:]) * 0.8)
    list2[i] = " ".join(list2[i]) + '\n'

with open(path2, 'r+') as file2:
    file2.writelines(list2)
