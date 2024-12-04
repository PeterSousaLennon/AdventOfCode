import os
import re as r
print(os.getcwd())
#Change this line to your directory for Day 1 
#os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day2") #Desktop
os.chdir("C:/Users/peter/OneDrive/Documents/Programming/Python/AdventOfCode2024/Day3") #Laptop

def readFile(name):
    fileLocation = name + ".txt"
    with open(fileLocation) as f:
        file = f.read().replace("\n", "")
    
    return file


def findMul(text):
    hits = r.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", text)
    return hits

def calcPart1(mul):
    for op in mul:
        if op[0] == "m":
            



filename = "input"
problem = readFile(filename)
mulList = findMul(problem)
calcPart1(mulList)

