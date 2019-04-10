import sys

### MyClippings.txt file path
fileName = sys.argv[1]

with open(fileName) as myClippingsFile:
    line = myClippingsFile.readline()
    while line:
	print(line)
        line = myClippingsFile.readline()
