class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
