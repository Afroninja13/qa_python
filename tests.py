import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()

class TestBooksCollector:
    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        books_collector.delete_book_from_favorites("Book1")
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Children's Book")
        books_collector.set_book_genre("Children's Book", "Мультфильмы")
        books = books_collector.get_books_for_children()
        expected_books = {"Book1"}
        assert set(books) != expected_books

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Book1", "Book2"]),
        ("Детективы", ["Book3"]),
        ("Мультфильмы", []),
    ])
    def test_get_books_with_specific_genre(self, books_collector, genre, expected_books):
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Фантастика")
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book2", "Фантастика")
        books_collector.add_new_book("Book3")
        books_collector.set_book_genre("Book3", "Детективы")
        assert books_collector.get_books_with_specific_genre(genre) == expected_books


@pytest.mark.parametrize("book_name, genre", [
    ("Book1", None),  # Добавление книги без жанра
    ("Children's Book", "Мультфильмы"),  # Добавление книги для детей
    ("Horror for Adults", "Ужасы"),  # Добавление книги с возрастным рейтингом
])
def test_add_new_book(books_collector, book_name, genre):
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    book_genre = books_collector.get_book_genre(book_name)
    expected_genre = '' if genre is None else genre
    assert book_genre == expected_genre

def test_get_list_of_favorites_books(books_collector):
    # Добавляем книги в избранное
    books_collector.add_new_book("Book1")
    books_collector.add_new_book("Book2")
    books_collector.add_book_in_favorites("Book1")
    books_collector.add_book_in_favorites("Book2")
    print(books_collector.get_list_of_favorites_books())

    # Получаем список избранных книг
    favorites = books_collector.get_list_of_favorites_books()

    # Проверяем, что метод возвращает ожидаемый список избранных книг
    assert favorites == ["Book1", "Book2"]







