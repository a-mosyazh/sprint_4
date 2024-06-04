# Описание тестов, содержащихся в test.py

### 1. Тесты для метода add_new_book:
 - test_add_new_book_add_one_book - успешное добавление одной книги в список books_genre. У книги нет жанра
 - test_add_new_book_name_is_invalid_book_is_not_added - в список books_genre не добавлены книги, наименования которых не удовлетворяют условию 0 < len(name) < 41
 - test_add_new_book_same_book_twice_only_once_added - при попытке добавления в список books_genre одной книги дважды книга добавлена только один раз

### 2. Тесты для метода set_book_genre:
 - test_set_book_genre_added_book_an_existing_genre - книге из списка books_genre добавлен жанр из списка genre
 - test_set_book_genre_book_is_not_in_the_list_genre_is_not_set - присвоение книге, не находящейся в списке books_genre, жанра из списка genre. Ни книга не жанр не добавлены в books_genre
 - test_set_book_genre_genre_does_not_exist_genre_in_not_set - присвоение книге из списка books_genre жанра, не находящегося в списке genre. Книге не присвоен жанр

### 3. Тесты для метода get_book_genre:
 - test_get_book_genre_one_book - успешное получение жанра книги из списка books_genre
 - test_get_book_genre_book_is_not_in_the_list_none_is_returned - получение жанра книги, отсутствующей в списке books_genre

### 4. Тесты для метода get_books_with_specific_genre:
 - test_get_books_with_specific_genre_one_fantasy_book - получение книги из списка books_genre, в котором находятся книги разных жанров. Возвращаются только книги с указанным жанром
 - test_get_books_with_specific_genre_no_books_by_genre_empty_list_returns - по указанному жанру в списке books_genre нет книг. Возвращается пустой список
 - test_get_books_with_specific_genre_genre_does_not_exist_empty_list_returns - при получении указывается жанр, не находящийся в списке genre. Возвращается пустой список

### 5. Тесты для метода get_books_genre:
 - test_get_books_genre_two_books - успешное получение списка books_genre, состоящего из двух книг

### 6. Тесты для метода get_books_for_children:
 - test_get_books_for_children_two_books_only_book_without_rating_returns - в списке books_genre есть подходящие и неподходящие детям книги, возвращаются только подходящие

### 7. Тесты для метода add_book_in_favorites:
 - test_add_book_in_favorites_one_book - успешное добавление одной книги в список favorites
 - test_add_book_in_favorites_book_is_not_in_list_book_is_not_in_favorites - добавление в список favorites книги, отсутствующей в списке books_genre. Книга не добавлена в favorites
 - test_add_book_in_favorites_same_book_twice_only_once_added - добавление одной и той же книги в список favorites дважды. Книга добавлена только один раз

### 8. Тесты для метода delete_book_from_favorites:
 - test_delete_book_from_favorites_one_book - успешное удаление книги из списка favorites
 - test_delete_book_from_favorites_book_is_not_in_favorites_favorites_remains - удаление книги, отсутствующей в списке favorites. Favorites остается прежним

### 9. Тесты для метода get_list_of_favorites_books:
 - test_get_list_of_favorites_books_one_book - получение списка favorites с одним элементом внутри