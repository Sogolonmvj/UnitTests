import datetime
import unittest

from model.person import Person


class TestPerson(unittest.TestCase):
    def test_calculate_age(self) -> None:
        person: Person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected: dict = {'name': 'Sogolon', 'age': 25}
        self.assertEqual(first=person.calculate_age(), second=expected)

    def test_name(self) -> None:
        person: Person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected: str = 'Sogolon'
        self.assertEqual(first=person.name, second=expected)

    def test_birthdate(self) -> None:
        person: Person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected: datetime = datetime.date(1997, 8, 1)
        self.assertEqual(first=person.birthdate, second=expected)

    def test_age(self) -> None:
        person: Person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected: int = 25
        self.assertEqual(first=person.calculate_age()["age"], second=expected)


if __name__ == '__main__':
    unittest.main()
