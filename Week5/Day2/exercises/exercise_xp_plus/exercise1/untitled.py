class FamilyMember:
    def __init__(self, member):
        self.member = member
    def __str__(self):
        return f"{self.member['name']}'s details:\n\tage:{self.member['age']}\n\tgender:{self.member['gender']}\n\tis child:{self.member['is_child']}"


class IncredibleFamilyMember(FamilyMember):
    def __str__(self):
        # return str(super()).replace(f"{self.member['name']}'s details:", f"{self.member['incredible_name']}'s details:\n\treal name:{self.member['name']}")
        return super().__str__() + f"\n\tincredible name:{self.member['incredible_name']}\n\tpower:{self.member['power']}"

# class Member():
    # class FamilyMember(FamilyMember):
        # pass

# class IncredibleMember():
    # class FamilyMember(IncredibleFamilyMember):
        # pass

class Family():
    def __init__(self, last_name, *members):
        self.last_name = last_name
        self.members = list(members)
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"it's a {'boy' if kwargs['gender'] == 'Male' else 'girl'}!")
    def is_18(self, name):
        return name in map(lambda item: item['name'],list(filter(lambda item: item['age'] >= 18, self.members)))
    def __print_members(self, Member):
        print(*map(lambda item: Member(item), self.members), sep="\n")
    def _print_members(self, Member):
        self.__print_members(Member)
    def print_members(self):
        self.__print_members(FamilyMember)
    def get_member(self, name):
        return list(filter(lambda item: item['name'] == name, self.members))

family = Family('Fuchs', {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False})

family.print_members()
print(family.is_18('Michael'))


class TheIncredibles(Family):
    # def __init__(self, *args):
        # super()(*args)
        # self.__args = args
    def use_power(self, name):
        if self.is_18(name): print(self.get_member(name)['power'])
    def incredible_presentation(self):
        self._print_members(IncredibleFamilyMember)

incredible_family = TheIncredibles('Parr', {'incredible_name':'Mr. Incredible', 'gender': 'Male', 'name': 'Robert', 'age':40, 'power': 'incredible strength, resistance, and enhanced senses', 'is_child' : False},{'incredible_name':'ElastiGirl', 'name':'Helen', 'gender': 'Female', 'age': 40, 'power': 'stretch for up 34 meters', 'is_child' : False})

incredible_family.print_members()
incredible_family.incredible_presentation()
incredible_family.born(**{'name': 'Jack', 'gender': 'Male', 'age':0,'power':'unknown power', 'incredible_name':'unknown name', 'is_child':True})

incredible_family.print_members()
incredible_family.incredible_presentation()
