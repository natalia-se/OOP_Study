from animal_class import Herbivore

class Visitors:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feedAnimal(self, animal):
        if isinstance(animal, Herbivore):
            animal.beFed(self)
        else:
            print(f"{self.name} cannot feed {animal.name}, it's a carnivore!")