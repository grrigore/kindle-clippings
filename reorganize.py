import sys
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)


# MyClippings.txt file path
fileName = sys.argv[1]

highlightSeparator = "==========\n"
highlights = []


with open(fileName, 'r+') as myClippingsFile:
    data = myClippingsFile.read()
    myClippingsFile.seek(0)
    myClippingsFile.write(highlightSeparator + data)
    highlights = data.split(highlightSeparator)
    highlights = highlights[:-1]
    for highlight in highlights:
        print(highlight + " ------ ")

createDirectory("My Clippings")

for highlight in highlights:
    bookTitle = highlight.split("(")[0]
    bookTitle = bookTitle[:-1] + '.txt'
    bookTitle = bookTitle.replace("\ufeff", "")
    with open("My Clippings/" + bookTitle, 'a') as bookHighlights:
        bookHighlights.write("\n" + highlight)
