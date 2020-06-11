from threading import Thread
import time

def test(i):
    print("---%d---"%i)
    time.sleep(1)

for i in  range(10):
    t = Thread(target=test,args=(i,))
    t.start()

