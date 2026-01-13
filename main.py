from biblioteca import Biblioteca, Book

objetobiblioteca = Biblioteca("central")

book1 = Book("Python", "Guido", 1)
book2 = Book("Java", "Gosling", 2)

objetobiblioteca.addb(book1)
objetobiblioteca.addb(book2)

objetobiblioteca.show()

print(book1.lend())
print(book1.lend())
book1.back()
print(book1.lend())