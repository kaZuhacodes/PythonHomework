class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} ({self.species}) says: {self.sound}!"
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        return f"{self.name} has laid an egg."

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")
    
    def shear(self):
        return f"{self.name} is being sheared for wool."

class Farm:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the farm.")
    
    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.species})")


farm = Farm()
cow = Cow("Bessie")
chicken = Chicken("Clucky")
sheep = Sheep("Dolly")

farm.add_animal(cow)
farm.add_animal(chicken)
farm.add_animal(sheep)

farm.show_animals()


print(cow.make_sound())
print(chicken.lay_egg())
print(sheep.shear())
