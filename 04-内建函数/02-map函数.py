def f1(x,y):
    return(x,y)

l1 = [0,1,2,3,4,5,6]
l2 = ['Sun','M','T','W','T','F','S']
l3 = map(f1,l1,l2)
print(list(l3))
