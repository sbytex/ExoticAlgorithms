import random
from threading import Thread
from copy import copy
from time import sleep


def is_sorted(l):
    n = l[0]
    for i in l[1:]:
        if i < n:
            return False
        n = i
    return True


def bogosort(list):
    l = copy(list)
    while not is_sorted(l):
        random.shuffle(l)
    print('Output:', l)


sleep_out = []


def delayed_output(n):
    sleep(n * 0.1)
    sleep_out.append(n)


def sleepsort(list):
    for n in list:
        Thread(target=lambda:delayed_output(n)).start()
    while len(sleep_out) < len(list):
        pass
    print('Output:', sleep_out)

