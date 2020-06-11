class Test(object):
    def __init__(self):
        self.__num = 100

t = Test()
t.__num = 200
print(t.__num)
