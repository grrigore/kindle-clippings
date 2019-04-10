import sys

### MyClippings.txt file path
fileName = sys.argv[1]

with open(fileName) as myClippingsFile:
    line = myClippingsFile.readline()
    firstLine = line
    cnt = 1
    while line:
        line = myClippingsFile.readline()
        if line == "==========\n":
            with open(firstLine + '.txt', 'a') as bookFile:
                bookFile.write('Hello\n')
            bookFile = myClippingsFile.readline()
        else:
            break
       # print("Line {}: {}".format(cnt, line.strip()))
       # line = myClippingsFile.readline()
       # cnt += 1
