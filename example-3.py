import multiprocessing as mp
import datetime
from time import time

global start_time


def start_f1(name):
    while time() < start_time: pass
    now = datetime.datetime.now()
    print("hello ", name)
    print("Current second: %d" % now.second)
    print("Current microsecond: %d" % now.microsecond)


def start_f2(name):
    print("hello")
    while time() < start_time: pass
    now = datetime.datetime.now()
    print("bye ", name)
    print("Current second: %d" % now.second)
    print("Current microsecond: %d" % now.microsecond)


if __name__ == '__main__':
    procs = []
    start_time = time() + 10

    p1 = mp.Process(target=start_f1, args=('bob',))
    p2 = mp.Process(target=start_f2, args=('sir',))
    procs.append(p1)
    procs.append(p2)


    p1.start()
    p2.join()
    # map(lambda x: x.start(), procs)
    # map(lambda x: x.join(), procs)
