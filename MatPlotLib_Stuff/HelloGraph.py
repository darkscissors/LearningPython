import matplotlib.pyplot as plt
import os
#x = 4
#y = 6
yOut = []
plt.ylabel('numbers or smth')
file = open(r'C:\Users\darks\Documents\GitHub\LearningPython\MatPlotLib_Stuff\z.txt')


def fileLength(file):
    with file as f:
        for i, l in enumerate(f):
            pass
    return i + 1

numCount = fileLength(file);
print(numCount)
file = open(r'C:\Users\darks\Documents\GitHub\LearningPython\MatPlotLib_Stuff\z.txt')
for x in range(0,numCount):
    y = file.readline(x)
    #print(y)
    yOut.append(y)
    #plt.plot(x,y)
    #print('test')

#for x1 in range(0,numCount):
    #plt.plot(x1,yOut[x1],'bo')

plt.plot(yOut)

plt.show()
