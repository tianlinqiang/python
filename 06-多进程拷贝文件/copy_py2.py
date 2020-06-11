#coding=utf-8
from multiprocessing import Pool,Manager
import os
import sys
def copyFileTask(name,oldFileName,newFileName,queue):
    fr = open(oldFileName+"/"+name)
    fw = open(newFileName+"/"+name,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)

def main():
    oldFileName = raw_input("请输入要复制的文件名：")
    newFileName = oldFileName+"复件"
    os.mkdir(newFileName)
    filenames = os.listdir(oldFileName)

    pool = Pool(5)
    queue = Manager().Queue()
    for name in filenames:
        pool.apply_async(copyFileTask,args=(name,oldFileName,newFileName,queue))
    num = 0.00
    allNum = len(filenames)
    while True:
        queue.get()
        num += 1.00
        copyRate = num/allNum
        a = "copy的进度是：%.2f%%s"%(copyRate*100)
        #print("\rcopy的进度是：%.2f%%"%(copyRate*100),end="",flush=True)
        sys.stdout.write('\r%s' %(a))
        sys.stdout.flush()
        if num == allNum:
            break
    print("\n已经copy完成了，感谢使用。")

if __name__ =="__main__":
   main()
