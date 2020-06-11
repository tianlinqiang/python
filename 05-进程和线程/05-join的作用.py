from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start()
p.join()  #等待子进程运行完，再运行主进程
print("---main---")


