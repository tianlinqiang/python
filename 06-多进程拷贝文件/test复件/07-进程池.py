from multiprocessing import Pool
import os
import random
import time

def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d"%(os.getpid(),num))
        time.sleep(1)

pool = Pool(5)
for i in range(10):
    print("---%d---"%i)
    print("...1....")
    pool.apply_async(worker,(i,))
    print("...2...")
pool.close()
pool.join()
