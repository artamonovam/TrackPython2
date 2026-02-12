
import doctest


class Message:
    """Класс, описывающий сообщение."""

    def __init__(self, user_id: str, text: str):
        """
        Создание объекта "Message"

        :param user_id: идентификатор пользователя
        :param text: текст сообщения

        Примеры:
        >>> msg = Message("user1", "Привет")
        >>> msg.user_id
        'user1'
        """
        ...

    def edit(self, new_text: str) -> None:
        """
        Изменение текста сообщения.

        :param new_text: новый текст

        Примеры:
        >>> msg = Message("user1", "Привет")
        >>> msg.edit("Пока")
        >>> msg.text
        'Пока'
        """
        ...

    def get_info(self) -> dict:
        """
        Получение информации о сообщении.

        :return: словарь с информацией

        Примеры:
        >>> msg = Message("user1", "Привет")
        >>> msg.get_info()['user_id']
        'user1'
        """
        ...


class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта "Book"

        :param title: название книги
        :param author: автор
        :param pages: количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Толстой", 100)
        >>> book.title
        'Война и мир'
        """
        ...

    def read_page(self, page: int) -> str:
        """
        Чтение страницы.

        :param page: номер страницы
        :return: содержимое страницы

        Примеры:
        >>> book = Book("Война и мир", "Толстой", 100)
        >>> book.read_page(1)
        'Страница 1'
        """
        ...

    def get_info(self) -> dict:
        """
        Получение информации о книге.

        :return: словарь с информацией

        Примеры:
        >>> book = Book("Война и мир", "Толстой", 100)
        >>> book.get_info()['pages']
        100
        """
        ...


class Stack:
    """Класс, описывающий стек (LIFO)."""

    def __init__(self, max_size: int = 10):
        """
        Создание объекта "Stack"

        :param max_size: максимальный размер стека

        Примеры:
        >>> stack = Stack(5)
        >>> stack.max_size
        5
        """
        ...

    def push(self, item) -> bool:
        """
        Добавление элемента в стек.

        :param item: элемент для добавления
        :return: True если добавлен, False если переполнен

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(1)
        True
        >>> stack.push(2)
        True
        >>> stack.push(3)
        False
        """
        ...

    def pop(self):
        """
        Удаление и возврат верхнего элемента.

        :return: верхний элемент

        Примеры:
        >>> stack = Stack()
        >>> stack.push(1)
        True
        >>> stack.push(2)
        True
        >>> stack.pop()
        2
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
