from random import randint


class Gene:
    def __init__(self, *args):
        self.val = args if args else bool(randint(0,1))
    def mutate(self):
        if type(self)().val:
            self.val = not self.val
    def __str__(self):
        return '1' if self.val else '0'


class Chromosome:
    def __init__(self, *args):
        self.val = [Gene() for _ in range(10)] if not args else args
    def mutate(self):
        for gene, flag in zip(self.val, type(self)().val):
            if flag:
                gene.mutate()
    def __str__(self):
        return ''.join([str(item) for item in self.val])

class DNA(Chromosome):
    def __init__(self,*args):
        self.val = args if args else [Chromosome() for _ in range(10)]


class Organism:
    def __init__(self, dna=DNA(),environment=randint(10,100)):
        self.dna = dna
        self.environment = environment
    def mutate(self):
        if self.environment >= randint(10, 100):
            self.dna.mutate()
    def check_only1s(self):
        return not '0' in str(self.dna)

organisms = [Organism(environment=100) for _ in range(1)]

loop = True
gen = 0
while loop:
    for organism in organisms:
        print(organism.dna)
        organism.mutate()
        if organism.check_only1s():
            loop = False
            break
    gen += 1

print(gen)
