class Library:
    def __init__(self, books=[]):
        self.books = books

    def addBook(self, book123):
        self.books.append(book123)

    def removeBook(self, name):
        for i in self.books:
            if i.name == name:
                self.books.remove(i)
    def is_book_exist(self, name):
        for book in self.books:
            if name == book.name:
                return True
        return False
    def is_autors_book_exist(self, autor_name):
        for book in self.books:
            if autor_name == book.autor:
                return True
        return False
    def printBooklist(self):
        if len(self.books) == 0:
            print("No books")
            return
        print("Book list:")
        for i in self.books:
            print(f"    name: {i.name}")
            print(f"    price: {i.price}")
            print(f"    category: {i.category}")
            print(f"    autor: {i.autor}")

