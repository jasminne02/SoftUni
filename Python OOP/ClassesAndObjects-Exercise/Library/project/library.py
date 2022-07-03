from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # author: [available books]
        self.rented_books = {}  # usernames: {book name: days to return}

    def get_book(self, author:str, book_name: str, days_to_return: int, user: User):
        for author_name, books in self.books_available.items():
            if book_name in books and author == author_name:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, info in self.rented_books.items():
            if book_name in info:
                return f'The book "{book_name}" is already rented and will be available in {info[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        return f"{user.username} doesn't have this book in his/her records!"
