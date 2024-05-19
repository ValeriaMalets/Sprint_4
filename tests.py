from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.set_book_genre('Гарри Поттер и Философский камень', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и Философский камень') == 'Фантастика'


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Тайная комната')
        collector.set_book_genre('Гарри Поттер и Тайная комната', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и Тайная комната') == 'Фантастика'

    import pytest
    @pytest.mark.parametrize('book_name',['Гарри Поттер и узник Азкабана','Гарри Поттер и Кубок Огня'])
    def test_get_books_with_specific_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert book_name in books


    import pytest
    @pytest.mark.parametrize('book_name',['Гарри Поттер и Орден Феникса','Гарри Поттер и Принц-полукровка'])
    def test_get_books_genre(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        expected = {book_name: ''}
        assert collector.get_books_genre() == expected


    def test_get_books_for_children_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Дары Смерти: ч.1')
        collector.add_new_book('Противостояние')
        collector.set_book_genre('Гарри Поттер и Дары Смерти: ч.1', 'Фантастика')
        collector.set_book_genre('Противостояние', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert  books_for_children == ['Гарри Поттер и Дары Смерти: ч.1']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Фантастические твари и где они обитают')
        collector.add_book_in_favorites('Фантастические твари и где они обитают')
        assert 'Фантастические твари и где они обитают' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Девушка с татуировкой дракона')
        collector.add_book_in_favorites('Девушка с татуировкой дракона')
        collector.delete_book_from_favorites('Девушка с татуировкой дракона')
        assert 'Девушка с татуировкой дракона' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Пролетая над гнездом кукушки')
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Пролетая над гнездом кукушки')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Пролетая над гнездом кукушки']


    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        long_name = 'ibtTest' * 15
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    import pytest
    @pytest.mark.parametrize('book_name', ['Дюна','Ведьмак', 'Хроники Нарнии'])
    def test_add_multiple_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()







