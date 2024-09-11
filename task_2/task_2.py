# Напишите класс Library, который управляет книгами. Класс должен поддерживать
# следующие методы:
# ● add_book(title): добавляет книгу в библиотеку.
# ● remove_book(title): удаляет книгу из библиотеки.
# ● list_books(): возвращает список всех книг в библиотеке.
# При попытке удалить книгу, которая не существует, должно выбрасываться исключение
# BookNotFoundError. Для тестирования используйте unitest
from error_task_2 import BookNotFoundError
class Library:
    def __init__(self, name):
        self.name = name
        self.list_all_books = []

    def add_book(self,title, author,pages):
        dict_book = {'title':title, 'author':author, 'pages':pages}
        self.list_all_books.append(dict_book)
    def remove_book(self,title, author):
        book_copy = self.list_all_books.copy()
        for i in range(len(book_copy)):
            if book_copy[i]['title'] == title and book_copy[i]['author'] == author:
                book =  self.list_all_books.pop(i)
                return f'Книга {book["title"]} автора {book["author"]} удалена из библиотеки имени {self.name}a'
        else:
            raise BookNotFoundError(title)


    def list_books(self):
        return '\n'.join([f'{book["title"]} {book["author"]} {book["pages"]} листа(ов)' for book in self.list_all_books])


if __name__ == '__main__':
    library = Library('Герцен')
    library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
    library.add_book("Герой нашего времени", "Лермонтов",102)
    library.add_book("Мцыри","Лермонтов",2)
    library.add_book("Вечера на хуторе", "Гоголь",45)
    print(library.list_books())
    print()
    print(library.remove_book("Мцыри", "Лермонтов"))
    print()
    print(library.list_books())
    print()
    try:
        print(library.remove_book('Bob','Jammy'))
    except BookNotFoundError as e:
        print(f'Выпала ошибка {e}')
