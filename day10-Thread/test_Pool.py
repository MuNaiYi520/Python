# 如果要启动大量的子进程,可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run Task %s (%s)...' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random() *3)
    end=time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Watting for all subprocess done...')
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    # Pool对象调用join()方法会等待所有子进程执行完毕
    p.join()
    print('All subprocess done .')
