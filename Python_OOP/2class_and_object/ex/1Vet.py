class Vet:
    animals = []

    def __init__(self, name):
        self.name = name

    def register_animal(self, animal_name):
        pass
    
    def unregister_animal(self, animal_name):
        pass

    def info(self):
        pass


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
