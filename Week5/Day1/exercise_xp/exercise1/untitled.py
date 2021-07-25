class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('tom', 20)
cat2 = Cat('jerry', 21)
cat3 = Cat('cat', 22)

def oldest_cat(*cats):
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

oldest = oldest_cat(cat1, cat2, cat3)
print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')
