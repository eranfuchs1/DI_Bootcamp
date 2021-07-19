class A:
    def __init__(self):
        self.val = set()
    def add(self, val):
        self.val.add(val)
    def __getitem__(self, key):
        return list(self.val)[key]
    def __setitem__(self, key, val):
        if key < len(self.val):
            self.val.remove(self.__getitem__(key))
        return val
    def __str__(self):
        return(str(list(self.val)))
    def __eq__(self, a):
        if type(a) == type(self):
            return a.val == self.val
        else:
            return a in self.val
