class basesingle(type):
    class_slv = {}

    def __call__(self, *args, **kwargs):
        if self not in self.class_slv:
            self.class_slv[self] = super(basesingle, self).__call__(*args,**kwargs)
        return self.class_slv[self]

class new_singleton(metaclass=basesingle):
    def __init__(self):
        self.name = 'Mark'
        self.age = 21
        self.gender = 'Male'

    def change_name(self, line:str):
        self.name = line

    def change_age(self, age:int):
        self.name = age

if __name__ == '__main__':
    person1 = new_singleton()
    person2 = new_singleton()
    print(person1)
    print(person2)
    print(person2.name)
    person1.change_name('Dima')
    print(person2.name)
