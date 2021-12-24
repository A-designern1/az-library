from book import Book

from library import Library

from autor import Autor

boooks = Library()
file = open('file.py', 'r')
for i in file:
    d = i.split(',')
    boook = Book(d[0], d[1], d[2], d[3])
    boooks.addBook(boook)
file.close()

while True:
    print("Enter command: ")
    command = input()
    if command == 'exit':
        print("Thank you, see you")
        file = open('file.py', 'w')
        for i in boooks.books:
            file.write(f'{i.name},{i.price},{i.category},{i.autor}')
        file.close()
        break

    elif command == 'add':
        print("Enter name:")
        name = input()
        print("Enter price:")
        price = input()
        print("Enter category:")
        category = input()
        print("Enter autor:")
        autor = input()

        book = Book(name, price, category, autor)
        autorName = Autor(autor)
        boooks.addBook(book)
    elif command == 'remove':
        print("Enter name:")
        name = input()
        boooks.removeBook(name)
    elif command == 'print':
        boooks.printBooklist()
    elif command == 'gimme':
        name = input()
        if boooks.is_book_exist(name):
            print('vot vasha kniga')
        else:
            print('etoy knigi net')
    elif command == 'gimme(autor)':
        name = input()
        if boooks.is_autors_book_exist(name):
            print('vot vasha kniga')
        else:
            print('etoy knigi net')
    else:
        print("Sorry, man. I don't have this command")
