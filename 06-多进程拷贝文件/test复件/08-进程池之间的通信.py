from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动 (%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

def write(q):
    print("write启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "tianlinqiang":
        q.put(i)

if __name__=="__main__":
    print("(%s)start"%os.getpid())
    q = Manager().Queue()
    po = Pool()

    po.apply(write,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()

    print("(%s)End"%os.getpid())
