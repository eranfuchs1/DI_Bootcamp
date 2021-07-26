class Age():
    def is_over18(self):
        return self.age >= 18

class Name():
    def show_details(self):
        print("Hello my name is " + self.name)


class Being(Age, Name):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person(Being):
    pass

class AnimalYears(Age):
    def __init__(self, animal_year):
        self.animal_year = animal_year
        self.refresh()
    def refresh(self):
        self.animal_years = self.age * self.animal_year
    def get_animal_years(self):
        return self.animal_years

class Animal(Being, AnimalYears):
    def __init__(self, name, age, animal_year):
        Being.__init__(self,name,age)
        AnimalYears.__init__(self, animal_year)


class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age, 4)

first_person = Person("John", 36)
print(first_person.is_over18())
first_person.show_details()
second_person = Person('David', 17)
print(second_person.is_over18())

cat1 = Cat('cat1', 20)
print(cat1.get_animal_years())
