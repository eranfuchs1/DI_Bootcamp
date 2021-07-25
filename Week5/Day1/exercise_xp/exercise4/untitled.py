class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(*self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            del self.animals[self.animals.index(animal_sold)]
    def sort_animals(self):
        self.animals.sort()
        self.animals = [list(filter(lambda animal: animal[0] == l, self.animals)) for l in sorted(list(set([animal[0] for animal in self.animals])))]
    def get_groups(self):
        for animal in self.animals:
            print(*animal)


ramat_gan_safari = Zoo('Ramat Gan Safari')

ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('giraffe')
ramat_gan_safari.add_animal('zebra')
ramat_gan_safari.add_animal('abc')
ramat_gan_safari.add_animal('abcd')
ramat_gan_safari.add_animal('babc')
ramat_gan_safari.add_animal('babcd')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('dog')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.get_animals()
