import random

def importBooks(filename):
    books = {}
    file = open(filename, 'r')
    for lineNumber, line in enumerate(file):
        bookData = line.rsplit().split(',')
        books[lineNumber] = {}
        books[lineNumber] = bookData[0]
        books[lineNumber] = bookData[1]
    file.close()
    return books

def importUsers(filename):
    users = {}
    currentUser = ''
    file = open(filename, 'r')
    for lineNumber, line in enumerate(file):
        userData = line.rsplit()
        if (lineNumber % 2) == 0:
            users[userData] = {}
            currentUser = userData
        else:
            ratings = userData.split(' ')
            for bookId, rating in enumerate(ratings):
                if int(rating) != 0:
                    users[currentUser][bookId] = int(rating)
    file.close()
    return users

def createNewUser(username, allUserRatings, library):
    allUserRatings[username] = {}
    print("Please rate some books:")
    booksToRate = library.keys()
    booksRemaining = int(len(library)*0.2)

    while booksRemaining > 0:
        if len(booksToRate) == 0:
            print("No more books to rate")
            break

        selectedBookId = random.choice(booksToRate)
        selectedBook = library[selectedBook]

        print("Please rate: " + selectedBook['title'] + " by " + selectedBook['author'] + " from 1-5 or 0  if you haven't read:")
        userRatingRealValue = {1:-5,2:-3,3:1,4:3,5:5}
        userRating = getValidInt(0,5)
        bookRating = userRatingRealValue.get(userRating)

        if bookRating != 0:
            allUserRatings[username][selectedBookId] = bookRating
            booksRemaining -= 1
    return

def getValidInt(minimum, maximum):
    return int(userInput)

def createNewUser(username, allUserRatings, library):
    allUserRatings[username] = {}






