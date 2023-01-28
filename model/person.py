import datetime


class Person:
    def __init__(self, name: str, birthdate: datetime) -> None:
        self.name = name
        self.birthdate = birthdate

    def calculate_age(self) -> dict:
        today: datetime = datetime.date.today()
        age: int = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return {"name": self.name, "age": age}
