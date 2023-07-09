# SuperFastPython.com
# example of multiprocessing program with freeze support
from time import sleep
from multiprocessing import Process
from multiprocessing import freeze_support
 
# function executed in a new child process
def task():
    # report message
    print('Hello from child process', flush=True)
    # block for a moment
    sleep(2)
 
# protect the entry point
if __name__ == '__main__':
    # add freeze support for multiprocessing
    freeze_support()
    # configure the child process
    child = Process(target=task)
    # start the child process
    child.start()
    # wait for the child process to terminate
    child.join()