def func(function):
    def func_in():
        ret = function()
        return ret
    return func_in
@func
def test():
    print("---test---")
    return "hahahaha"

res = test()
print("test return is %s" %res)
