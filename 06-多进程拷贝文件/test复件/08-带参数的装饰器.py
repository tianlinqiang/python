def func_arg(args):
    def func(function):
        def func_in():
            print("开始装饰...-args=%s" %args)
            function()
        return func_in
    return func
#1.先执行func_args("heihei")函数，这个函数返回的结果是func的引用
#2.@func
#3.使用@func进行装饰

@func_arg("heihei")
def test():
    print("---test---")

test()
