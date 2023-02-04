class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, pages: int, name=None, author=None):
        super().__init__(name=name, author=author)

        @property
        def prop_pages() -> int:
            return self._pages

        @prop_pages.setter
        def prop_name(_pages: int) -> None:
            if not pages > 0:
                raise ValueError
            if not isinstance(pages, int):
                raise TypeError

        self._pages = pages


class AudioBook(Book):
    def __init__(self, duration: float, name=None, author=None):
        super().__init__(name=name, author=author)

        @property
        def prop_duration() -> float:
            return self._duration

        @prop_duration.setter
        def prop_name(_duration: float) -> None:
            if not duration > 0:
                raise ValueError
            if not isinstance(duration, float):
                raise TypeError

        self._duration = duration

    @property
    def prop_name(self) -> str:
        return self._name

    @prop_name.setter
    def prop_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    @property
    def prop_author(self) -> str:
        return self._author

    @prop_author.setter
    def prop_author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError
        self._author = author


book1 = PaperBook(500, "Обелиск", "Ремарк")
print(book1)
book2 = AudioBook(500, "Обелиск", "Ремарк")
print(book2)
book3 = Book("Обелиск", "Ремарк")
print(book3)
