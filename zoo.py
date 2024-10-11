from animal_class import Lion, Elephant, Giraffe
from visitors_class import Visitors
from zoo_day import zooDay

lions = [
    Lion(name="Simba", age=4, energyLevel=90, strength=70),
    Lion(name="Nala", age=3, energyLevel=85, strength=65),
    Lion(name="Mufasa", age=8, energyLevel=100, strength=90, isAlpha=True),
    Lion(name="Scar", age=6, energyLevel=30, strength=75),
    Lion(name="Kiara", age=2, energyLevel=70, strength=50)
]

elephants = [
    Elephant(name="Dumbo", age=10, energyLevel=80, size="large", herdSize=5),
    Elephant(name="Ella", age=8, energyLevel=75, size="medium", herdSize=5),
    Elephant(name="Babar", age=15, energyLevel=90, size="large", herdSize=5),
    Elephant(name="Tantor", age=6, energyLevel=70, size="medium", herdSize=5),
    Elephant(name="Manny", age=18, energyLevel=85, size="large", herdSize=5)
]

giraffes = [
    Giraffe(name="Ginny", age=6, energyLevel=80, size="tall", neckLength=7),
    Giraffe(name="George", age=5, energyLevel=75, size="tall", neckLength=8),
    Giraffe(name="Gigi", age=4, energyLevel=70, size="tall", neckLength=6),
    Giraffe(name="Gerald", age=7, energyLevel=85, size="tall", neckLength=9),
    Giraffe(name="Grace", age=3, energyLevel=20, size="tall", neckLength=6.5)
]

animals = lions + elephants + giraffes

visitors = [
    Visitors(name="Alice", age=30),
    Visitors(name="Bob", age=24),
    Visitors(name="Charlie", age=40),
    Visitors(name="Diana", age=35),
    Visitors(name="Eve", age=28)
]

zooDay(animals, visitors)