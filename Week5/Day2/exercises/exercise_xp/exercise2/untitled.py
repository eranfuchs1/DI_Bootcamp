from functools import reduce
class FighterAnimal:
    def fight(self, other_animal):
        return self if self.run_speed() * self.weight > other_animal.run_speed() * other_animal.weight else other_animal


class Dog(FighterAnimal):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return self.weight/self.age*10
    def fight(self, other_dog):
        return super().fight(other_dog).name

if __name__ == '__main__':
    dogs = [Dog('tom', 20, 20), Dog('jerry', 21, 30), Dog('mouse', 22, 22)]
    print(reduce(FighterAnimal.fight, dogs).name)
    print(list(map(Dog.fight, dogs, [dogs[-1]] + dogs[:-1])))
