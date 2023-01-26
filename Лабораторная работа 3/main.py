class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f'Книга "{self.name}". Автор "{self.author}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """ Дочерний класс - бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_value) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_value, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_value


class AudioBook(Book):
    """ Дочерний класс - аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_value) -> None:
        """Устанавливает длительность аудиокниги."""
        if not isinstance(new_value, float):
            raise TypeError("Длительность книги должна быть типа float")
        if new_value <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self._duration = new_value

