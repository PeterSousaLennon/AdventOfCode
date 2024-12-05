import os
print(os.getcwd())
#Change this line to your directory for Day 1 
os.chdir("C:/Users/Peter/Desktop/Software Projects/Python/AdventOfCode/Day4")

def readFile(name):
    fileLocation = name + ".txt"
    with open(fileLocation) as f:
        file = f.read().splitlines()
    
    return file

def checkNextLetter(puzzle, target, x, y, dir = -1):
    pass





def search(puzzle):

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "X":
                checkNextLetter(puzzle, "M", i, j)


    return result


def padding(puzzle):
    for i in range(len(puzzle)):
        puzzle[i] = "." + puzzle[i] + "."

    puzzle.insert(0, "."*len(puzzle[0]))
    puzzle.append("."*len(puzzle[0]))
    
    return puzzle


name = "myfile"
wordsearch = readFile(name)

#print(wordsearch)
paddedPuzzle = padding(wordsearch)

for i in range(len(paddedPuzzle)):
    print(paddedPuzzle[i])
