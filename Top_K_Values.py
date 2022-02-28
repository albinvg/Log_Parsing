"""
## Find the top 5 IPs that have been repeated in decending order
## Only calculate for response code of 5XX 

## This is the sample file to be parsed
2022-02-26T14:55:35+00:00 501 6.191.20.203
2022-02-26T14:55:35+00:00 203 155.80.11.146
2022-02-26T14:55:35+00:00 500 218.122.175.69
2022-02-26T14:55:35+00:00 502 153.188.15.192
2022-02-26T14:55:35+00:00 501 210.84.82.56
2022-02-26T14:55:35+00:00 203 183.42.111.186
2022-02-26T14:55:35+00:00 201 199.35.211.130
2022-02-26T14:55:35+00:00 500 9.126.119.77
2022-02-26T14:55:35+00:00 203 3.82.155.50
2022-02-26T14:55:35+00:00 202 24.109.82.117
2022-02-26T14:55:35+00:00 201 15.240.32.22
2022-02-26T14:55:35+00:00 204 33.145.145.175
"""

path = "Drive:\\Folder\\folder\\File.01.log"

with open(path, 'r') as f:
    list1 = f.readlines()

dict1 = {}                                      # Track the number oftimes an item/IP has been repeated
frequency = [[] for i in range (len(list1))]    # Create an empty list to track in reverse order (List of lists length of lines in file)
output = []
k = 5

#create a list of lists for the input file. Delimiter is space
for i in range(len(list1)):
    list1[i] = list1[i].split()
    
    #create dictionary that maps the IPs to number of times they were repeated
    if list1[i][1][:1] == "5" and list1[i][2][:3] != "127":
        if list1[i][2] not in dict1:
            dict1[list1[i][2]] = 1
        else:
            dict1[list1[i][2]] += 1

#create freq list. The index of freq list is the number of times the IP was repeated. THe Value in that index contains all those IPs
for IP in dict1:
    index = dict1[IP]
    frequency[index].append(IP)


#create a new list that has the top K IPs along with the number of times they were repeated. In decending order. 
for i in range(len(frequency) - 1, 0, -1):
    if frequency[i] != []:
        output.append([frequency[i], i])
        if len(output) == k:
          print (output)

