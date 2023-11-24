import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()

def test_add_new_book_success(books_collector):
    # Проверка успешного добавления новой книги без указания жанра
    books_collector.add_new_book("New Book")
    assert books_collector.get_book_genre("New Book") == ''

@pytest.mark.parametrize("existing_book, genre, expected_genre", [
    ("Book1", "Фантастика", "Фантастика"),  # Установка жанра для существующей книги
    # ("Nonexistent Book", "Жанр", ''),  # Попытка установить жанр для несуществующей книги
    ("Book2", "Неизвестный жанр", '')  # Попытка установить неизвестный жанр
])
def test_set_book_genre(books_collector, existing_book, genre, expected_genre):
    books_collector.add_new_book(existing_book)
    books_collector.set_book_genre(existing_book, genre)
    assert books_collector.get_book_genre(existing_book) == expected_genre


@pytest.mark.parametrize("book_name, expected_genre", [
    ("Book1", "Фантастика"),
    ("Children's Book", "Мультфильмы"),
    ("Horror for Adults", "Ужасы"),
])
def test_get_book_genre(books_collector, book_name, expected_genre):
    # Подготовка: Добавление книг с соответствующими жанрами
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, expected_genre)

    # Тест: Получение жанра книги
    assert books_collector.get_book_genre(book_name) == expected_genre


def test_get_books_with_specific_genre(books_collector):
    # Подготовка: Добавление книг с разными жанрами
    books_collector.add_new_book("Book1")
    books_collector.set_book_genre("Book1", "Фантастика")
    books_collector.add_new_book("Book2")
    books_collector.set_book_genre("Book2", "Детективы")

    # Тест: Получение книг с определенным жанром
    books_with_specific_genre = books_collector.get_books_with_specific_genre("Фантастика")

    # Проверка, что в списке только книги заданного жанра
    assert "Book1" in books_with_specific_genre
    assert "Book2" not in books_with_specific_genre



def test_get_books_genre(books_collector):
    # Проверка корректности получения словаря с жанрами всех книг
    books_collector.add_new_book("Book1")
    books_collector.set_book_genre("Book1", "Фантастика")
    books_collector.add_new_book("Book2")
    books_collector.set_book_genre("Book2", "Ужасы")

    expected_books_genre = {"Book1": "Фантастика", "Book2": "Ужасы"}
    assert books_collector.get_books_genre() == expected_books_genre


def test_get_books_for_children(books_collector):
    # Получение списка книг, подходящих для детей (без возрастного рейтинга)
    books_collector.add_new_book("Children's Book")
    books_collector.set_book_genre("Children's Book", "Мультфильмы")
    books_collector.add_new_book("Adult's Book")
    books_collector.set_book_genre("Adult's Book", "Ужасы")

    assert books_collector.get_books_for_children() == ["Children's Book"]


def test_add_and_delete_book_in_favorites(books_collector):
    # Добавление и удаление книги из избранного
    books_collector.add_new_book("Book1")
    books_collector.add_book_in_favorites("Book1")
    books_collector.add_new_book("Book2")
    books_collector.add_book_in_favorites("Book2")

    # Проверка добавленных книг в избранное
    assert books_collector.get_list_of_favorites_books() == ["Book1", "Book2"]

    # Удаление книги из избранного
    books_collector.delete_book_from_favorites("Book1")
    assert books_collector.get_list_of_favorites_books() == ["Book2"]

    # Попытка удалить несуществующую книгу из избранного
    books_collector.delete_book_from_favorites("Nonexistent Book")
    assert books_collector.get_list_of_favorites_books() == ["Book2"]

@pytest.mark.parametrize("book_name", [
    "",        # Длина названия 0 (не добавится в словарь)
    "X" * 41,  # Длина названия 41 (не добавится в словарь)
    "X" * 42   # Длина названия 42 (не добавится в словарь)
])
def test_add_new_book_invalid_length(books_collector, book_name):
    # Проверка добавления книги с недопустимой длиной названия
    books_collector.add_new_book(book_name)
    assert book_name not in books_collector.get_books_genre()


@pytest.mark.parametrize("book_name", [
    "X",      # Длина названия 1 (добавится в словарь)
    "XY",     # Длина названия 2 (добавится в словарь)
    "X" * 39, # Длина названия 39 (добавится в словарь)
    "X" * 40  # Длина названия 40 (добавится в словарь)
])
def test_add_new_book_valid_length(books_collector, book_name):
    # Проверка добавления книги с разрешённой длиной названия
    books_collector.add_new_book(book_name)
    assert book_name in books_collector.get_books_genre()

def test_get_list_of_favorites_books(books_collector):
    # Добавляем книги в избранное
    books_collector.add_new_book("Book1")
    books_collector.add_new_book("Book2")
    books_collector.add_book_in_favorites("Book1")
    books_collector.add_book_in_favorites("Book2")

def test_add_book_with_age_rating_to_children_list(books_collector):
    # Добавляем книгу с возрастным рейтингом
    books_collector.add_new_book("Mature Book")
    books_collector.set_book_genre("Mature Book", "Ужасы")

    # Проверяем, что книга с возрастным рейтингом не попала в список книг для детей
    assert "Mature Book" not in books_collector.get_books_for_children()
