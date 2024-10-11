import random
from termcolor import colored
class Animal:
    def __init__(self, name, age, energyLevel):
        self.name = name
        self.age = age
        self.energyLevel = energyLevel

    def eat(self):
        if self.energyLevel < 85:
            self.energyLevel += 15
            print("Come later! I'm eating right now.")
    
    def sleep(self):
        self.energyLevel += 15
        print("Be quiet! I'm sleeping!")

    def makeSound(self):
        print("Making some sound")

    def beFedByPersonal(self):
        self.energyLevel += 30 


class Herbivore(Animal):
    def __init__(self, name, age, energyLevel, diet, size, haveHorns):
        super().__init__(name, age, energyLevel)
        self.diet = diet
        self.size = size
        self.haveHorns = haveHorns

    def beFed(self, visitor):
        print(f"{self.name} is being fed by {visitor.name}.")
        if self.energyLevel < 95:
            self.energyLevel += 5
        else:
            print(f"{self.name} is nor hungry.") 

class Carnivore(Animal):
    def __init__(self, name, age, energyLevel, sleepPattern, strength):
        super().__init__(name, age, energyLevel)
        self.sleepPattern = sleepPattern
        self.strength = strength
    
    def hunt(self, prey):
        if self.energyLevel < 90:
            print(colored(f"{self.name} is hunting {prey.name}."), "yellow")
            self.energyLevel += 10
            prey.energyLevel = 0
        else:
            print(f"{self.name} is not hungry for hunting.")

class Lion(Carnivore):
    def __init__(self, name, age, energyLevel, strength, prideSize=5, isAlpha=False):
        super().__init__(name, age, energyLevel, sleepPattern="night", strength=strength)
        self.prideSize = prideSize
        self.isAlpha = isAlpha

    def makeSound(self):
        print(f"{self.name} the lion roars mightily!")
    
    def socialBehavior(self):
        if self.isAlpha:
            print(f"{self.name} is the alpha and leads the pride!")
        else:
            print(f"{self.name} interacts with the pride, bonding with other lions.")
    def play(self):
        play_actions = [
            "pouncing on another lion",
            "chasing another lion",
            "play wrestling with a pride member",
            "swatting at another lion with its paw",
            "tugging on another lion's tail",
            "batting at a stick or bone",
            "sneaking up and stalking another lion",
            "rolling around in the grass",
            "jumping on rocks or small trees",
            "splashing in a waterhole",
            "having a mock roaring contest",
            "hiding and ambushing another lion"
        ]
        action = random.choice(play_actions)
        if self.energyLevel > 50:
            print(f"{self.name} is {action}!")
            self.energyLevel -= 15
        else:  
            self.sleep()
            print(f"{self.name} is tired!")

    def sleep(self):
        if self.energyLevel < 85:
            print(f"{self.name} is resting.")
            self.energyLevel += 15
        else:
            self.play()

class Elephant(Herbivore):
    def __init__(self, name, age, energyLevel, size, herdSize = 10):
        super().__init__(name, age, energyLevel, diet = "grass", size = size, haveHorns = "no")
        self.herdSize = herdSize
        
    def makeSound(self):
        print(f"{self.name} the elephant trumpets loudly!")
    
    def eat(self):
        print(f"{self.name} is using its trunk to grab food.")
        self.energyLevel += 15
    
    def play(self):
        if self.energyLevel > 50:
            playType = ["chasing other calves", "rolling in the mud", "splashing water", "wrestling with trunks", "pushing logs around"]
            action = random.choice(playType)
            print(f"{self.name} is {action}")
        else:  
            self.sleep()
            print(f"{self.name} is tired!")
    
    def sleep(self):
        if self.energyLevel < 90:
            print(f"{self.name} is sleeping standing up for short periods.")
            self.energyLevel += 10
        else:
            self.play()

class Giraffe(Herbivore):
    def __init__(self, name, age, energyLevel, size, neckLength = 3):
        super().__init__(name, age, energyLevel, diet = "leaves from tall trees", size = size, haveHorns = "no")
        self.neckLength = neckLength

    def makeSounds(self):
        print (f"{self.name} the giraffe hums softly.")

    def eat(self):
        print(f"{self.name} is using its {self.neckLength}-meter neck to eat leaves from tall trees.")
    
    def play(self):
        if self.energyLevel > 50:
            play_actions = [
                "necking with another giraffe",
                "running in circles",
                "chasing another giraffe",
                "playfully head-butting another giraffe",
                "exploring and nibbling on branches",
                "kicking the ground",
                "stretching its neck to reach higher branches",
                "playing with rocks or sticks",
                "splashing water at a waterhole",
                "interacting with birds"
            ]
            action = random.choice(play_actions)
            print(f"{self.name} is {action}!")
            self.energyLevel -= 15
        else:
            self.sleep()

    def sleep(self):
        if self.energyLevel < 90:
            print(f"{self.name} is sleeping briefly while standing.")
            self.energyLevel += 8
        else:
            self.play()

    