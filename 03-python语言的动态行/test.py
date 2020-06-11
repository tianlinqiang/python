def setnum():
    a,b = 0, 1 
    for i in range(0,5):
        yield b
        a,b =b, a+b


