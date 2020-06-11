def func(function):
    print("---func---")
    def func_in():
        print("---func_in---")
        res = function()
        print("---function---")
        return res
    print("---func---")
    return func_in
@func
def test():
    print("---test---")
    return "hahah"

ret = test()
print("test return is %s" %ret)
