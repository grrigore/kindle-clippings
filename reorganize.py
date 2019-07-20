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

# Read from MyClippings.txt
with open(fileName, 'r+') as myClippingsFile:
    data = myClippingsFile.read()
    highlights = data.split(highlightSeparator)
    highlights = highlights[:-1]

createDirectory("My Clippings")

# Write in directory
for highlight in highlights:
    bookTitle = highlight.split("\n")[0]
    bookTitle = bookTitle + '.txt'
    bookTitle = bookTitle.replace("\ufeff", "")
    bookTitle = bookTitle.replace("\u0000", "")
    with open("My Clippings/" + bookTitle, 'a') as bookHighlights:
        bookHighlights.write(highlight + "\n")
