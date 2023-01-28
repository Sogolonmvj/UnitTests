import datetime

from model.person import Person


def start():
    return Person("Sogolon", datetime.date(1997, 8, 1))


if __name__ == '__main__':
    print(start().calculate_age())
