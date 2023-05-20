"""
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv 
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal
"""

with open(path1, 'r+') as f:
    list1 = f.readlines()
with open(path2, 'r+') as f:
    list2 = f.readlines()


for i in range(len(list2)):
    list2[i] = list2[i].split(',')
    #need to fix the '\n' character at end

    NAME = list2[i][0]
    STRIDE_LENGTH = list2[i][1]
    STANCE = list2[i][2]

    if STANCE == 'bipedal':
        dinosaur_dict[NAME] = [STRIDE_LENGTH, STANCE]


for i in range(len(list1)):
    list1[i] = list1[i].split(',')

    NAME = list1[i][0]
    STRIDE_LENGTH = list1[i][1]
    STANCE = list1[i][2]
    g = 9.8 m/s^2            # need to fix the unit
    SPEED = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)


    if NAME in dinosaur_dict.keys():
        dinosaur_dict[NAME].append(STRIDE_LENGTH)
        dinosaur_dict[NAME].append(STANCE)
        dinosaur_dict[NAME].append(SPEED)


dinosoar_list = list(dinosaur_dict.items())

dinosoar_list.sort(key=lambda x:x[1][4], reverse=True)
#sorted in decending order of speed

for i in dinosoar_list:
    print(dinosoar_list[0])
