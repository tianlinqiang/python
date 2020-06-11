def setnum():
    a,b = 0, 1 
    for i in range(0,50):
        yield b  #yield的作用：打印b ,让程序停一下
        a,b =b, a+b

c = setnum()
for num in c:
    print(num)
