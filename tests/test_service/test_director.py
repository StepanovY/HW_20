from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()  # Фикстура с моком для DirectorDAO
def director_dao():
    director_dao = DirectorDAO(None)

    jonh = Director(id=1, name='jonh')
    kate = Director(id=2, name='kate')
    tarantino = Director(id=3, name='tarantino')

    director_dao.get_one = MagicMock(return_value=tarantino)
    director_dao.get_all = MagicMock(return_value=[jonh, kate, tarantino])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:  # Класс с тестами для DirectorService
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        data = {
            'name': 'Kriss'
        }

        director = self.director_service.create(data)

        assert director is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        data = {
            'id': 3,
            'name': 'Kventin'
        }

        self.director_service.update(data)
