from threading import Thread
import time
g_num = 0
def work1():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("---work1---%d"%g_num)
    
def work2():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("---work2---%d"%g_num)

t1 = Thread(target = work1)
t1.start()
#time.sleep(1) 如果不休眠，会导致work1执行了一半然后执行work2很有可能
#会g_num还没变得时候就执行，导致少加好多次
t2 = Thread(target = work2)
t2.start()
