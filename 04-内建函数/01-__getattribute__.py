#__getattribute__ 此方法会在对象调用属性的时候先调用这个方法，然后这个方法的返回值会指向本该调用的函数去调用
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    def __getattribute__(self,obj):
        print("====1>%s" %obj)
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            temp = object.__getattribute__(self,obj)
            print("====>2%s" %str(temp))
            return temp
    def show(self):
        print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)
s.show()
