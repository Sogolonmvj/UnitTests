import datetime
import unittest

from model.person import Person


class TestPerson(unittest.TestCase):
    def test_calculate_age(self):
        person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected = {'name': 'Sogolon', 'age': 25}
        self.assertEqual(person.calculate_age(), expected)

    def test_name(self):
        person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected = 'Sogolon'
        self.assertEqual(person.name, expected)

    def test_birthdate(self):
        person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected = datetime.date(1997, 8, 1)
        self.assertEqual(person.birthdate, expected)

    def test_age(self):
        person = Person("Sogolon", datetime.date(1997, 8, 1))
        expected = 25
        self.assertEqual(person.calculate_age()["age"], expected)


if __name__ == '__main__':
    unittest.main()
