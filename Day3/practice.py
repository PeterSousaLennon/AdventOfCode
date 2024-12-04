import os
import re as r
print(os.getcwd())
#Change this line to your directory for Day 1 
os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day3") #Desktop
#os.chdir("C:/Users/peter/OneDrive/Documents/Programming/Python/AdventOfCode2024/Day3") #Laptop

def readFile(name):
    fileLocation = name + ".txt"
    with open(fileLocation) as f:
        file = f.read().replace("\n", "")
    
    return file


def findMul(text):
    hits = r.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", text)
    return hits

def calcPart1(mul):
    print(mul[0])
    print(mul[0][mul[0].find("(")+1:])
    print(mul[0][:-1])
    
    values = []
    x = []
    for data in mul:
        if data[0] == "m":
            #values.append([data[data.find("(")+1:], data[:-1]])
            x = data.split(",")
            values.append([int(x[0][x[0].find("(")+1:]), int(x[1][:-1])])
    
    print(values)

filename = "input"
problem = readFile(filename)
mulList = findMul(problem)
calcPart1(mulList)

