import time
from pympler import asizeof
import random
start_time = time.time()

N=1000
total=0


def calcut(s, c):
    list = []
    list.append(s)
    prcUp = random.uniform(0.08, 0.12)
    p = random.uniform(0.4, 0.7)
    prcDown = random.uniform(0.07, 0.1)
    for m in range(c):
        next = []
        for i in range(len(list)):
            next.append(list[i] * (1 + prcUp))
        next.append(list[-1] * (1 - prcDown))
        list = next
    for k in range(len(list)):
        if list[k] - 110 > 0:
            list[k] = list[k] - 110
        else:
            list[k] = 0
    while len(list) > 1:
        next = []
        for j in range(len(list) - 1):
            next.append((list[j] * (1 - p)) + (list[j + 1] * (p)))
        list = next
    return list[0]


for l in range(N):
    total += calcut(100, 36)


print('значение',total/N)
print(asizeof.asizeof(N) + asizeof.asizeof(l) + asizeof.asizeof(total))
print('time', time.time() - start_time)

print(dir())