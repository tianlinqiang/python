#coding=utf-8
def w1(func):
    def inner():
        print("---正在验证---")
        if True:
            print("---验证通过---")
            func()
        else:
            print("---验证失败---")
    return inner
@w1   #@w1 --> f1 = w1(f1)
def f1():
    print("---f1---")
@w1
def f2():
    print("---f2---")

#f1 = w1(f1)
f1()
#f2 = w1(f2)
f2()
