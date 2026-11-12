class Student:
    def __init__(self, name: str, phone: str, email: str, group: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self) -> str:
        return f"Name = {self.name}, Phone = {self.phone}, Email = {self.email}, Group = {self.group}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group,
        }