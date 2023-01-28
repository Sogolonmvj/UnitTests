import datetime

from model.person import Person


def start() -> Person:
    return Person(name="Sogolon", birthdate=datetime.date(1997, 8, 1))


if __name__ == '__main__':
    print(start().calculate_age())
