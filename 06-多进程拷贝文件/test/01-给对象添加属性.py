class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

laowang = Person("laowang",50)
print(laowang.name)
print(laowang.age)
laowang.addr = "深圳"
print(laowang.addr)
