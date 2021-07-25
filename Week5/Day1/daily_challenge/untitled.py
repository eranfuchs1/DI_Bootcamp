class Animals():
    def __init__(self):
        self.animals = {}
    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount
    def __str__(self):
        return ('\n' * 3) + ''.join([f'{animal} : {self.animals[animal]}\n' for animal in self.animals]) + ('\n' * 3)
    def get_animal_types(self):
        return list(set([animal for animal in self.animals]))

class Farm(Animals):
    def __init__(self, name):
        self.name = name
        Animals.__init__(self)
    def __str__(self):
        return f"{self.name}'s farm"
    def get_info(self):
        return f"{self}{Animals.__str__(self)}   E-I-E-I-O!"
    def get_short_info(self):
        return f"{self} has " + ' '.join([f"{animal}s" for animal in self.get_animal_types()])

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())


print(macdonald.get_short_info())
