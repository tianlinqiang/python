def func(function):
    def func_in(*args, **kwargs):
        print("---正在装饰---")
        res = function(*args, **kwargs)
        return res
    return func_in
@func
def test():
    print("---test---无参数，无返回值的装饰器")
test()
@func
def test2():
    print("有返回值得装饰器")
    return "hahaha"
res = test2()
print(res)

@func
def test3(a, b, c):
    print("带有参数的返回值")
    print("返回的参数为%d,%d,%s" %(a, b, c) )
test3(3,4,'abc')
