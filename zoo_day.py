import random
from termcolor import colored
from animal_class import Carnivore, Herbivore

def zooDay(animals, visitors):
    print("One more day in our Zoo!")
    
    huntedAnimals = []
    print("Animals' Play and Status:")
    for animal in animals:
        animal.play()
        animal.eat()
        animal.sleep()
        if isinstance(animal, Carnivore):
            herbivores = [a for a in animals if isinstance(a, Herbivore)]
            if len(herbivores) > 2:  # Ensure there are more then 2 herbivores in the zoo
                prey = random.choice(herbivores)
                huntedAnimals.append(prey)
                animal.hunt(prey)
                # Remove the hunted prey from the animals list
                animals.remove(prey) 
                print(colored(f"Hunting {prey.name}", "green"))
            else:
                print(colored(f"The staff saves Herbivore", "red"))

    for visitor in visitors:
        print(f"{visitor.name} is interacting with the animals.")
        for animal in random.sample(animals, len(animals)//2):
            visitor.feedAnimal(animal)

    for animal in animals:
        if animal.energyLevel < 20:
            print(f"{animal.name} needs help from personal")
            animal.beFedByPersonal()

    print("The day has ended at the zoo!")
    for a in huntedAnimals:
        print(colored(f"{a.name} was hunted", "red"))
    
    