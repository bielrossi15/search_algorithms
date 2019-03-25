from b_search import binary_search
from index_search import index_search
from linear_search import linear_search
from interpolation_search import interpolation_search
import matplotlib.pyplot as plt
import time
import random

def time_check(choice: str, ite: int):
    l = []
    lim = 10000000
    if choice == 'sorted':
        for i in range(lim):
            l.append(random.randint(0, lim))
        l.sort()

    elif choice == 'normalized':
        for i in range(lim):
            l.append(i)

    inter = []
    seq = []
    bnry = []
    indexed = []


    for i in range(0, ite):
        value = random.randint(0, lim)
        if(choice == 'normalized'):
            start2 = time.clock()
            ret1 = interpolation_search(l, value)
            end2 = time.clock()
            if ret1 == True:
                time2 = end2 - start2
                inter.append(time2)

        start1 = time.clock()
        ret2 = linear_search(l, value)
        end1 = time.clock()
        if ret2 == True:
            time1 = end1 - start1
            seq.append(time1)

        start3 = time.clock()
        ret3 = binary_search(l, value)
        end3 = time.clock()
        if ret3 == True:
            time3 = end3 - start3
            bnry.append(time3)

        start4 = time.clock()
        ret4 = index_search(l, value)
        end4 = time.clock()
        if ret4 == True:
            time4 = end4 - start4
            indexed.append(time4)


    plt.xlabel('Iterations')
    plt.ylabel('Time')
    if len(inter) != 0:
        plt.plot(inter, color='red', label='interpolation')
    plt.plot(seq, color='green', label='sequential')
    plt.plot(bnry, color='blue', label='binary')
    plt.plot(indexed, color='purple', label='indexed')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    it = int(input())
    method = input()
    time_check(method, it)