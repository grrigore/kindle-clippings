import sys
import os
import re
import json


def createJsonFile(books):
    with open('books.json', 'w', encoding="utf-8-sig") as jsonFile:
        json.dump(books, jsonFile, ensure_ascii=False, indent=4)


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def getAuthor(bookTitle):
    bracketsContent = re.findall('(?<=\\().+?(?=\\))', bookTitle)
    author = bracketsContent[-1]
    return author


def getAuthors(bookTitle):
    bracketsContent = re.findall('(?<=\\().+?(?=\\))', bookTitle)
    authors = bracketsContent[-1]
    return authors.split(authorSeparator)


def getTitle(highlightTitle, authors):
    authorsAsString = (authorSeparator).join(authors)
    title = highlightTitle.split("(" + authorsAsString + ")")[0]
    return title.strip()


def getHighlightDetails(highlight):
    highlightParts = highlight.split(highlightDetailsSeparator)
    text = highlight.split("\n\n")[1].strip()
    page = int(highlightParts[0].split("\n")[1].replace(
        highlightPageMetaData, '').strip())
    location = highlightParts[1].replace(highlightLocationMetaData, "").strip()
    date = highlightParts[2].split("\n\n")[0].strip()
    return Highlight(text, page, location, date)


class Book:
    def __init__(self, id, title, authors, highlights=[]):
        self.id = id
        self.title = title
        self.authors = authors
        self.highlights = highlights


class Highlight:
    def __init__(self, text, page, location, date):
        self.text = text
        self.page = page
        self.location = location
        self.date = date

fileName = sys.argv[1]

highlightSeparator = "==========\n"
authorSeparator = "; "
highlightDetailsSeparator = "|"
highlightPageMetaData = "- Your Highlight on page"
highlightLocationMetaData = "Location"
books = []

with open(fileName, 'r+', encoding='utf-8-sig') as myClippingsFile:
    data = myClippingsFile.read().replace(u'\ufeff', '')
    highlights = data.split(highlightSeparator)
    highlights = highlights[:-1]

for highlight in highlights:
    # get highlight title - contains book title and authors
    highlightTitle = highlight.split("\n")[0]
    # get book authors from current hightlight
    bookAuthors = getAuthors(highlightTitle)
    # get book title from current hightlight
    bookTitle = getTitle(highlightTitle, bookAuthors)
    # get highlight details from current hightlight
    bookHighlightDetails = getHighlightDetails(highlight).__dict__
    bookHighlights = []
    bookHighlights.append(bookHighlightDetails)
    # generate book id
    bookId = str(hash(highlightTitle))[1:]
    book = Book(bookId, bookTitle, bookAuthors, bookHighlights).__dict__
    books.append(book)

createJsonFile(books)
