class BookNotFoundError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Внимание! Внимание! Ошибка!\n' \
               f'Вы пытаетесь удалить книгу {self.name}, которой не существует'