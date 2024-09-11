import unittest
from task_2 import Library
from error_task_2 import BookNotFoundError


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library('Герцен')
        # self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        # self.library.add_book("Герой нашего времени", "Лермонтов",102)
        # self.library.add_book("Мцыри","Лермонтов",2)
        # self.library.add_book("Вечера на хуторе", "Гоголь",45)

    def test_1(self):
        self.library.add_book('Десять дней, которые изменили мир', 'Джон Уик', 99)
        self.assertTrue(self.library.list_all_books == [{'title': 'Десять дней, которые изменили мир',
                                                         'author': 'Джон Уик',
                                                         'pages': 99}])

    def test_2(self):
        self.assertRaises(BookNotFoundError, self.library.remove_book, 'Карлсон', 'Астрет Лингрен')

    def test_3(self):
        self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        self.assertEqual(self.library.list_books(), 'Сказка о рыбаке и рыбке Пушкин 109 листа(ов)')

    def test_4(self):
        self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        self.library.add_book("Герой нашего времени", "Лермонтов", 102)
        self.library.remove_book("Герой нашего времени", "Лермонтов")
        self.assertEqual(self.library.list_all_books, [{'title': 'Сказка о рыбаке и рыбке',
                                                        'author': "Пушкин",
                                                        'pages': 109}])

    def test_5(self):
        self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        self.library.remove_book('Сказка о рыбаке и рыбке', "Пушкин")
        self.library.add_book("Мцыри", "Лермонтов", 2)
        self.assertEqual(self.library.list_all_books, [{'title':"Мцыри",
                                                        'author':"Лермонтов",
                                                        'pages': 2}])
    def test_6(self):
        self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        self.library.add_book("Мцыри", "Лермонтов", 2)
        self.assertIn({'title':"Мцыри",'author':"Лермонтов",'pages':2}, self.library.list_all_books)

    def test_7(self):
        self.library.add_book('Сказка о рыбаке и рыбке', "Пушкин", 109)
        self.library.add_book("Мцыри", "Лермонтов", 2)
        self.assertNotIn({'title':'Карлсон', 'author':'Астрет Лингрен','pages':9},self.library.list_all_books)


if __name__ == '__main__':
    unittest.main()
