# -*- coding:utf-8 -*-

import random
rooms = [[],[],[]]
teachers = ["A","B","C","D","E","F","G","H"]
for name in teachers:
    randomNum = random.randint(0,2)
    rooms[randomNum].append(name)
i = 1
for room in rooms:
    print ("123344"),
    for name in room:
        #这里在print后面加一个逗号，可以不换行显示
        print(name),
    print("")
    i += 1
