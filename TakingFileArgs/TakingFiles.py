import sys

try:
    with open(sys.argv[1],'r') as inputFile:
        print(inputFile.read())
except IndexError as e:
    print('Error, you probably dident add a file as an arguement \nError: ', e)
