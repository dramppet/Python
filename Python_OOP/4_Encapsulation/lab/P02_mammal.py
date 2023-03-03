class Mammal:
    kingdom = "animals"
    def __init__(self, name, type_mammal, sound):
        self.name = name
        self.type_mammal = type_mammal
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.kingdom

    def info(self):
        return f"{self.name} is of type {self.type_mammal}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
