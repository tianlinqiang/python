def w1(fn):
    def b1():
        print ("---1---")
        return "<b>" + fn() + "</b>"
    return b1

def w2(fn):
    def b1():
        print("---2---")
        return "<i>" + fn() + "</i>"
    return b1
@w1  #test=w1(test)
@w2 #test=w2(test)
def test():
    print ("---3---")
    return "hello-world"

res = test()
print(res)
