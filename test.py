import pytest

from main import BooksCollector


class TestBooksCollector:

    # переменные используются для успешного наполнения books_genre
    fantasy_book = 'Ranking of Kings'
    fantasy_genre = 'Фантастика'
    horror_book = 'Solo Leveling'
    horror_genre = 'Ужасы'

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        assert len(collector.books_genre) == 1 and collector.books_genre[self.fantasy_book] == ''

    @pytest.mark.parametrize(
        'books',
        [
            '',
            'Rascal Does Not Dream of Bunny Girl Senpai'
        ]
    )
    def test_add_new_book_name_is_invalid_book_is_not_added(self, books):
        collector = BooksCollector()
        collector.add_new_book(books)
        assert len(collector.books_genre) == 0

    def test_add_new_book_same_book_twice_only_once_added(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.add_new_book(self.fantasy_book)
        assert len(collector.books_genre) == 1

    def test_set_book_genre_added_book_an_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        assert collector.books_genre[self.fantasy_book] == self.fantasy_genre

    def test_set_book_genre_book_is_not_in_the_list_genre_is_not_set(self):
        collector = BooksCollector()
        not_added_book = 'One Piece'
        collector.set_book_genre(not_added_book, self.fantasy_genre)
        assert collector.books_genre.get(not_added_book) is None

    def test_set_book_genre_genre_does_not_exist_genre_in_not_set(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, 'Adventure')
        assert collector.books_genre[self.fantasy_book] == ''

    def test_get_book_genre_one_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        assert collector.get_book_genre(self.fantasy_book) == self.fantasy_genre

    def test_get_book_genre_book_is_not_in_the_list_none_is_returned(self):
        collector = BooksCollector()
        not_added_book = 'One Piece'
        assert collector.get_book_genre(not_added_book) is None

    def test_get_books_with_specific_genre_one_fantasy_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.add_new_book(self.horror_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.set_book_genre(self.horror_book, self.horror_genre)
        list_of_books = collector.get_books_with_specific_genre(self.fantasy_genre)
        assert len(list_of_books) == 1 and list_of_books[0] == self.fantasy_book

    def test_get_books_with_specific_genre_no_books_by_genre_empty_list_returns(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        assert collector.get_books_with_specific_genre(self.horror_genre) == []

    def test_get_books_with_specific_genre_genre_does_not_exist_empty_list_returns(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Adventure') == []

    def test_get_books_genre_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.add_new_book(self.horror_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.set_book_genre(self.horror_book, self.horror_genre)
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_two_books_only_book_without_rating_returns(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.add_new_book(self.horror_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.set_book_genre(self.horror_book, self.horror_genre)
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1 and children_books[0] == self.fantasy_book

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.add_book_in_favorites(self.fantasy_book)
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_book_is_not_in_list_book_is_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites(self.fantasy_book)
        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_same_book_twice_only_once_added(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.add_book_in_favorites(self.fantasy_book)
        collector.add_book_in_favorites(self.fantasy_book)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.add_book_in_favorites(self.fantasy_book)
        collector.delete_book_from_favorites(self.fantasy_book)
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_book_is_not_in_favorites_favorites_remains(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.add_book_in_favorites(self.fantasy_book)
        collector.delete_book_from_favorites(self.horror_book)
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.add_new_book(self.fantasy_book)
        collector.set_book_genre(self.fantasy_book, self.fantasy_genre)
        collector.add_book_in_favorites(self.fantasy_book)
        assert len(collector.get_list_of_favorites_books()) == 1
