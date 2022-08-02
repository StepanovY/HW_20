from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()  # Фикстура с моком для MovieDAO
def movie_dao():
    movie_dao = MovieDAO(None)

    venom = Movie(id=1, title='venom', year=2020, rating=7)
    shine = Movie(id=2, title='shine', year=1980, rating=8)

    movie_dao.get_one = MagicMock(return_value=venom)
    movie_dao.get_all = MagicMock(return_value=[venom, shine])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:  # Класс с тестами для MovieService
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        data = {
            'title': 'Western',
            'year': 2022,
            'rating': 6
        }

        movie = self.movie_service.create(data)

        assert movie is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        data = {
            'id': 2,
            'title': 'Ups',
            'year': 2028
        }

        self.movie_service.update(data)
