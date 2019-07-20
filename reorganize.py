import sys
import os
import re


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)


def getAuthor(bookTitle):
    bracketsContent = re.findall('(?<=\\().+?(?=\\))', bookTitle)
    author = bracketsContent[-1]
    return author


# MyClippings.txt file path
fileName = sys.argv[1]

highlightSeparator = "==========\n"
highlights = []
authors = []

# Read from MyClippings.txt
with open(fileName, 'r+') as myClippingsFile:
    data = myClippingsFile.read()
    highlights = data.split(highlightSeparator)
    highlights = highlights[:-1]

createDirectory("My Clippings")

# Write in directory
for highlight in highlights:
    highlightTitle = highlight.split("\n")[0]
    author = getAuthor(highlightTitle)
    authors.append(author)
    bookTitle = highlightTitle.split("(" + author + ")")[0]
    print("Author:" + author + " Title: " + bookTitle)
    bookTitle = bookTitle[:-1] + '.txt'
    bookTitle = bookTitle.replace("\ufeff", "")
    bookTitle = bookTitle.replace("\u0000", "")
    with open("My Clippings/" + bookTitle, 'a') as bookHighlights:
        bookHighlights.write(highlight + "\n")
