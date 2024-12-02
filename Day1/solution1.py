import os
print(os.getcwd())
#Change this line to your directory for Day 1 
os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day1")

def readFile(name):
    fileLocation = name + ".txt"
    f = open(fileLocation, "r")
    
    list1 = []
    list2 = []
    count = 0

    for line in f:
        #list1.append(int(line[0]))
        #list2.append(int(line[4]))
        list1.append(int(line[:5]))
        list2.append(int(line[8:]))
    
    f.close()
    return [list1, list2]

def sortLists(list):
    return sorted(list)

bothLists = readFile("input")
sortedLists = []
sortedLists.append(sortLists(bothLists[0]))
sortedLists.append(sortLists(bothLists[1]))

#Calc distance between the sorted list
totalDist = 0
for i in range(len(sortedLists[0])):
    totalDist += abs(sortedLists[0][i] - sortedLists[1][i])

print(totalDist)


#Calc similarity score by counting how many an element in list1 appears in list2 and multiplying the element by the count
totalSim = 0
for i in range(len(sortedLists[0])):
    totalSim += sortedLists[0][i] * sortedLists[1].count(sortedLists[0][i])

print(totalSim)