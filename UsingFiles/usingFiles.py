import os



#file = open(r'C:\Users\darks\Documents\GitHub\LearningPython\UsingFiles\z.txt')
sum = 0
path = r'C:\Users\darks\Documents\GitHub\LearningPython\UsingFiles\z.txt'
#file = open(path, 'r')

#this function returns the file at designated path
def getFile(path):
    return open(path,'r')

#this function goes through each line in the file and counts it
def getLineCount(path):
    lineCount = 0
    with getFile(path) as file:
        lines = file.readlines()
        for line in lines:
            lineCount+=1
    file.close()
    return lineCount

#we use this function in order to add each line up and print the sum
for line in getFile(path):
    sum = sum + int(line)
print('sum = ',sum)

#we use the get file function once again because python needs to seek back to the top of the file, it must be re-called
print(getLineCount(path))
