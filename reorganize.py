import sys

### MyClippings.txt file path
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

for highlight in highlights:
    bookTitle = highlight.split("(")[0]
    bookTitle = bookTitle.replace("\ufeff", "")
    bookTitle = bookTitle[:-1] + '.txt'
    with open(bookTitle, 'a') as bookHighlights:
        bookHighlights.write("\n" + highlight)
