import time
from pympler import asizeof
import random

start_time = time.time()



S = 100
tot_s = 0
n = 1000
p = random.uniform(0.4, 0.7)
for k in range(n):
    # print(S)
    # print(tot_s)
    tot_s = tot_s + S
    #tot_s = round(tot_s, 2)
    S = 100
    for i in range(1, 3 * 12 + 1):
        if random.uniform(0, 1) > p:
            prcUp = random.uniform(0.08, 0.12)
            S *= 1 + prcUp  # наверх
            #S = round(S, 2)
            # print('месяц %d увеличение на %d%%. Стало %s' % (i, prcUp*100, S))
        else:
            prcDown = random.uniform(0.07, 0.1)
            S *= 1 - prcDown
            #S = round(S, 2)
            # print('месяц %d уменьшение на %d%%. Стало %s' % (i, prcDown*100, S))

if tot_s // n > 116:

    print(tot_s // n)
    print('Сделка выгодна. Цена опциона %s ' % (tot_s // n - 116))
else:
    print("Сделка невыгодна.")


print(asizeof.asizeof(p) + asizeof.asizeof(S) + asizeof.asizeof(prcUp) + asizeof.asizeof(i) + asizeof.asizeof(
    prcDown) + asizeof.asizeof(tot_s) + asizeof.asizeof(k)+asizeof.asizeof(n))
print(time.time() - start_time)
