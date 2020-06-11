class Test(object):
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        print("---getNum---")
        return self.__num

    @num.setter
    def num(self,newNum):
        print("---setNum---")
        self.__num = newNum
t=Test()

#print(t.getNum())
#t.setNum(10000)

#print(t.getNum())

print("----------------------------------")
t.num = 50
print (t.num)

