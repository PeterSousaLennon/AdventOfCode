import os
print(os.getcwd())
#Change this line to your directory for Day 1 
#os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day1")
os.chdir("C:/Users/peter/OneDrive/Documents/Programming/Python/AdventOfCode2024/Day2")

def readFile(name):
    fileLocation = name + ".txt"
    f = open(fileLocation, "r")

    reportLevels = [[]]

    #Reads each line of the text file, removing the spaces and covert into ints
    for line in f:
        temp = line.replace(" ", "")
        #reportLevels.append([int(item) for item in temp])
        values = []
        for i in range(len(temp)):
            if temp[i].isdigit() == True:
                values.append(int(temp[i]))
        reportLevels.append(values)

    reportLevels.pop(0)
    return reportLevels

def checkLevels(reportLine):
    safeLevels = True
    lastdiff = 0
    currentdiff = 0
    i = 0

    #for i in range(len(reportLine) - 1):
    while safeLevels == True and i < len(reportLine):
        currentdiff = reportLine[i] - reportLine[i+1]

        if abs(currentdiff) <= 3 and abs(currentdiff) > 0:
            if currentdiff > 0 and lastdiff > 0:
                print("We are increasing")
            elif currentdiff < 0 and lastdiff < 0:
                print("We are decreasing")
            else:
                print("We are hectic!")
                safeLevels = False
        
        i += 1

        print(reportLine[i])

report  = readFile("TestInput")
checkLevels(report[0])


