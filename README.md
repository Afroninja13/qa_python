# qa_python_4
## Метод add_new_book
### test_add_new_book_success:
#### Проверка успешного добавления книги
### test_add_new_book_invalid_length:
#### Проверка попытки добавления книги с невалидной длиной названия. Граничные значения убраны в параметризацию
### test_add_new_book_valid_length:
#### Проверка попытки добавления книги с валидной длиной названия. ГЗ также убраны в параметризацию
## Метод set_book_genre
### test_add_book_with_age_rating_to_children_list:
#### Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей.
### test_add_children_book_to_genre:
#### Проверка, что книги с возрастным рейтингом не попадают в список книг для детей.
### test_set_book_genre:
#### Успешная установка жанра для книги, если книга существует и её жанр входит в список доступных жанров.
##### Тестовые данные также убраны в параметризацию.
### test_get_book_genre_existing_book:
#### Получение жанра для существующей книги.
#### Ожидаемые тестовые данные убраны в парметризацию.
### test_get_book_genre_non_existing_book:
#### Получение жанра для отсутствующей книги.
## Метод get_books_with_specific_genre
### test_get_books_with_specific_genre_existing_genre:
#### Получение списка книг для существующего жанра.
### test_get_books_with_specific_genre_non_existing_genre:
#### Получение пустого списка книг для отсутствующего жанра.
## Метод get_books_for_children
### test_get_books_for_children
#### Проверка корректности списка книг, подходящих для детей.
## Методы add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books
### test_add_and_delete_book_from_favorites
#### Проверка добавления и удаления книг из избранного.
