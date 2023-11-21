# qa_python
## Метод add_new_book
### test_add_new_book_without_genre: Проверка добавления книги без указания жанра.
### test_add_children_book_to_genre: Проверка, что книги с возрастным рейтингом не попадают в список книг для детей.
### test_add_book_with_age_rating_to_children_list: Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей.
## Метод set_book_genre
### test_set_book_genre: Успешная установка жанра для книги, если книга существует и её жанр входит в список доступных жанров.
## Метод get_book_genre
### test_get_book_genre_existing_book: Получение жанра для существующей книги.
### test_get_book_genre_non_existing_book: Получение жанра для отсутствующей книги.
## Метод get_books_with_specific_genre
### test_get_books_with_specific_genre_existing_genre: Получение списка книг для существующего жанра.
### test_get_books_with_specific_genre_non_existing_genre: Получение пустого списка книг для отсутствующего жанра.
## Метод get_books_for_children
### test_get_books_for_children: Проверка корректности списка книг, подходящих для детей.
## Методы add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books
### test_add_and_delete_book_from_favorites: Проверка добавления и удаления книг из избранного.
