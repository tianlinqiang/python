import types
class Person(object):
    def __init__(self,newName):
        self.name = newName

def run(self):
    print("%s在跑" %self.name)

def eat(self):
    print("%s在吃" %self.name)

laowang = Person("老汪")

print(laowang.name)
laowang.run = types.MethodType(run, laowang)
laowang.eat = types.MethodType(eat, laowang)
laowang.run()
laowang.eat()
