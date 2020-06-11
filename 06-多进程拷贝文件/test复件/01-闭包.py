def test(number):
    print ("---1---")
    def test_in(a):
        print("---2---")
        print (number+a)
    print ("---3---")
    return test_in

res = test(100)

print ("--------------------")
res(1)
res(10)
res(100)
