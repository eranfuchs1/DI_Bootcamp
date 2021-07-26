from random import choice
from untitled import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *args):
        print(self.name, *args, 'all play together')
    def do_a_trick(self):
        print(self.name, choice(["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]))


if __name__ == '__main__':
    dog = PetDog('tom', 20, 20)
    dog.train()
    dog.play('jerry', 'mouse')
    dog.do_a_trick()
