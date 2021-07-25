class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog('Rex', 50)

print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)


print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

print(davids_dog.name if davids_dog.height > sarahs_dog.height else sarahs_dog.name)
