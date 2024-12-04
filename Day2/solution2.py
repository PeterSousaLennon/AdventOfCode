import os
print(os.getcwd())
#Change this line to your directory for Day 1 
os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day2")
#os.chdir("C:/Users/peter/OneDrive/Documents/Programming/Python/AdventOfCode2024/Day2")

def readFile(name):
    fileLocation = name + ".txt"
    f = open(fileLocation, "r")

    reportLevels = [[]]

    #Reads each line of the text file, removing the spaces and covert into ints
    for line in f:
        temp = [int(entry) for entry in line.split() if entry.isdigit()]
        reportLevels.append(temp)

    f.close()
    reportLevels.pop(0)
    return reportLevels

def checkLevels(reportLine):
    safeLevels = True
    firstPass = True
    lastdiff = 0
    currentdiff = 0
    i = 0
    
    #for i in range(len(reportLine) - 1):
    while safeLevels == True and i < len(reportLine) - 1:
        currentdiff = reportLine[i] - reportLine[i+1]

        if firstPass == False:
            if abs(currentdiff) <= 3 and abs(currentdiff) > 0:
                if currentdiff > 0 and lastdiff > 0:
                    #print("We are increasing")
                    safeLevels = True
                elif currentdiff < 0 and lastdiff < 0:
                    #print("We are decreasing")
                    safeLevels = True
                else:
                    #print("We are hectic!")
                    safeLevels = False
            else:
                #print("We are mental!")
                safeLevels = False
        else:
            if abs(currentdiff) <= 3 and abs(currentdiff) > 0:
                #print("We are Safe")  
                safeLevels = True             
            else:
                #print("We are dangerous!")
                safeLevels = False
            firstPass = False
        
        lastdiff = currentdiff
        i += 1

    return safeLevels

report  = readFile("input")
print(report[0])

count = 0
for entries in report:
    for i in range(len(entries)):
        temp = entries[:]
        temp.pop(i)
        if checkLevels(temp) == True:
            count += 1
            break

print("Number of safe reports:")
print(count)

