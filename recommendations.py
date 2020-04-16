import random

def importBooks(filename):
    books = {}
    file = open(filename, 'r')
    for lineNumber, line in enumerate(file):
        bookData = line.rstrip().split(',')
        books[lineNumber] = {}
        books[lineNumber]['author'] = bookData[0]
        books[lineNumber]['title'] = bookData[1]
    file.close()
    return books

def importUsers(filename):
    users = {}
    currentUser = ''

    file = open(filename, 'r')
    for lineNumber, line in enumerate(file):
        userData = line.rstrip()
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
    print ("As you're new, please rate a few books " + username + ":")
    booksToRate = library.keys()
    booksRemaining = int(len(library)*0.2)

    while (booksRemaining > 0):
        if len(booksToRate) == 0:
            print "We've run out of books to ask you to rate!"
            print "For more accurate reccomendations you might need to read a few more books!"
            break

        selectedBookId = random.choice(booksToRate)
        selectedBook = library[selectedBookId]
        
        booksToRate.remove(selectedBookId)

        print "\n Please rate", booksRemaining,"more books!\n"
        print "How many stars would you give", selectedBook["title"], "by", selectedBook["author"] + "?"
        print "Please enter a number from 1-5, or enter 0 if you haven't read this book."
        userRatingRealValue = {1:-5,2:-3,3:1,4:3,5:5}
        userRating = getValidInt(0,5)
        bookRating = userRatingRealValue.get(userRating)

        if(bookRating != 0):
            allUserRatings[username][selectedBookId] = bookRating
            booksRemaining -= 1
    return

def getValidInt(minimum, maximum):
    userInput = ""
    valid = False
        
    while(not valid):
        userInput = raw_input()
        if userInput.isdigit():
            if int(userInput) >= minimum and int(userInput) <= maximum:
                valid = True
            else:
                print("Error! Please only enter integers in the range:" + str(minimum) + "to" + str(maximum))
        else:
            print("Error! Please only enter integers in the range:" + str(minimum) + "to" + str(maximum))
            
    return int(userInput)

def compareUsers(user1, user2, allUserRatings):

    if user1 == user2:
        return float('inf')

    user1Ratings = allUserRatings[user1]
    user2Ratings = allUserRatings[user2]
    dotProduct = 0
    sharedBooks = set(user1Ratings.keys()).intersection(user2Ratings.keys())

    for book in sharedBooks:
        dotProduct += user1Ratings[book]*user2Ratings[book]

    return dotProduct

def getSimilarUsers(username, allUserRatings):
    similarUsers = allUserRatings.keys()
    similarUsers.sort(key=lambda x: compareUsers(username, x, allUserRatings), reverse=True)
    similarUsers.pop(0)

    return similarUsers

def findRecommendations(currentUser, numberOfRecommendations, similarUsers, allUserRatings, library):
    recommendations = []
    recommendationsGiven = 0
    finalRecommendations = []

    for user in similarUsers:
        for bookId, rating in allUserRatings[user].iteritems():
            if (rating >= 3 and not (bookId in [pair[0] for pair in recommendations]) and not (bookId in allUserRatings[currentUser].keys())):
                recommendations.append((bookId,user))
                recommendationsGiven += 1

            if (recommendationsGiven >= numberOfRecommendations):
                for recommendation in recommendations:
                    book = library[recommendation[0]]
                    finalRecommendations.append("Recommendation by " + str(recommendation[1]) + ": " + book["title"] + " by " + book["author"])
                return finalRecommendations

def output(filename, data):
    file = open(filename, 'w')
    for entry in data:
        file.write(entry + '\n')
        print entry
    file.close()

def main(users, library):
    print "Please enter your name:"
    username = raw_input().strip()

    if username == "":
        print("Error! Invalid entry.")
        return True

    if not(username in users.keys()):
        createNewUser(username, users, library)
        
    print "How many book recommendations would you like?"
    numberOfRecommendations = getValidInt(1, len(library))
    similarUsers = getSimilarUsers(username, users)
    finalRecommendations = findRecommendations(username, numberOfRecommendations, similarUsers, users, library)
    print("\n" + "Your recommendations are:" + "\n")
    output("output.txt", finalRecommendations)
    print("\n" + "Would you like to start from the beginning? (y/n)")

    response = raw_input().lower()
    
    if response == "y":
        print "-------------------------------------------------------------"
        main(userRatings, books)
    print("Exiting...")
    exit()

books = importBooks('books.txt')
userRatings = importUsers("ratings.txt")

main(userRatings, books)


