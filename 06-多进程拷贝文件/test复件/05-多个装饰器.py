def func(functionName):
    print("---fun-1----")
    def func_in(*args, **kwargs):
        print("---func---")
        functionName(*args, **kwargs)
        print("---func_in--2--")
    print("---func--2---")
    return functionName
@func
def test(a,b,c):
    print("---test-a=%d,b=%d,c=%d--" %(a,b,c))
@func
def test2(a,b,c,d,e):
     print("---test-a=%d,b=%d,c=%d,d=%d,e=%d--" %(a,b,c,d,e))
test(11,12,13)
test2(1,2,3,4,5)
