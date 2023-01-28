import datetime


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return {"name": self.name, "age": age}
