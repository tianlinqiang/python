import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello,%s (in %s)' %(std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread,args=('tlq',),name='ThreadA')
t2 = threading.Thread(target = process_thread,args=('田林强',),name='ThreadB')
t1.start()
t2.start()
