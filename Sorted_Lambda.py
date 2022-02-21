path = "C\\directory\\directory" + "\\Filename.txt"

#read logs into a list using 'readlines'
with open(path, 'r') as f:
    File = f.readlines()

#using ',' as a delimiter separate each line (ie; each item in the File list)  into a nested list.
for i in range(len(File)):
    File[i] = File[i].split(',')
    File[i][3] = File[i][3][:-1]    ##### remove the '\n' character at the end of each line

# sort the content of the files (except 1st line) based on the 4th column.
output = sorted(File[1:], key=lambda x: int(x[3]))    ### remember that the items in the sublist are strings. So covert them to integers to sort
print(output)
