class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, books: list):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
