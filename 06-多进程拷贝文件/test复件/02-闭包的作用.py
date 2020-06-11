def test(a,b):
    def test_in(x):
        return a*x+b
    
    return test_in
line1 = test(1,1)
line2 = test(2,4)

print(line1(1))
print(line2(1))
