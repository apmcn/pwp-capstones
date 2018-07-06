class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        ratingValue = 0
        for rating in self.books.values():
            if rating != None:
               ratingValue += rating
        return ratingValue / len(self.books)


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The book {title} ISBN has been updated".format(title=self.title))

    def add_rating(self, rating):
        if isinstance(rating, int) and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True

    def get_average_rating(self):
        ratingValue = 0
        for rating in self.ratings:
            ratingValue += rating
        return ratingValue / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):  
        if self.books.get(book) == None and book.isbn != None and not self.check_unique_isbn(book.isbn):
           print("Isbn {isbn} not unique for book {book}, book not being added to collection.".format(isbn=book.isbn, book=book.title))
        else:
            try:
              self.users[email]
              user = self.users[email]
              user.read_book(book, rating)
              if rating != None:
                 book.add_rating(rating)
              if self.books.get(book) == None:
                 self.books[book] = 1
              else:
                   self.books[book] += 1
            except KeyError:
              print("No user with email {email}!".format(email=email))
                             
    def check_unique_isbn(self, isbn):
        for book in self.books.keys():
            if book.isbn == isbn:
                return False
        return True

    
    def add_user(self, name, email, user_books=None):
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("Email {email} for user {name} is invalid, user not added.".format(email=email, name=name))
        else:
          try:
              self.users[email]
              print("User with email {email} already exists".format(email=email))
          except KeyError:
              user = User(name, email)
              self.users[email] = user
              if user_books != None:
                 for book in user_books:
                     self.add_book_to_user(book, email)


    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def highest_rated_book(self):
        highestRating = 0
        highestRatedBook = []
        for book in self.books.keys():
            highestRating = self.highest_rated(book, highestRatedBook, highestRating)
        return highestRatedBook
    
    def most_positive_user(self):
        highestRating = 0
        mostPositiveUser = []
        for user in self.users.values():
            highestRating = self.highest_rated(user, mostPositiveUser, highestRating)
        return mostPositiveUser

    def highest_rated(self, rateObject, highestRatedObject, highestRating):
        returnRating = rateObject.get_average_rating()
        if returnRating > highestRating and len(highestRatedObject) > 0:
           highestRatedObject.clear()
        if returnRating >= highestRating:
            highestRating = returnRating
            highestRatedObject.append(rateObject)
        return highestRating
        

    def get_most_read_book(self):
        mostRead = 0
        mostReadBook = []
        for book, count in self.books.items():
            if count > mostRead and len(mostReadBook) > 0:
                mostReadBook.clear()
            if count >= mostRead:
                mostRead = count
                mostReadBook.append(book)                      
        return mostReadBook








    


          



    
