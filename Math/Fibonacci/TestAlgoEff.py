from datetime import datetime, timedelta
from time import sleep

def fib01(n):
    if n == 0: return 0
    if n <= 2: return 1

    m, t = fib01(int(n/2)), fib01(2*int(n/2)-1)
    l, r = fib01(int(n/2)-1), fib01(int(n/2)+1)
    if n % 2 == 0:
        return m * (l + r)
    if n % 2 == 1:
        return m * (l + r) + t

memo = {}
def fib02(n):
    if n == 0: return 0
    if n <= 2: return 1
    if n in memo: return memo[n]

    m, t = fib02(int(n/2)), fib02(2*int(n/2)-1)
    l, r = fib02(int(n/2)-1), fib02(int(n/2)+1)
    if n % 2 == 0:
        memo[n] = m * (l + r)
        return memo[n]
    if n % 2 == 1:
        memo[n] = m * (l + r) + t
        return memo[n]

def fib03(n):
    if n == 0: return 0
    a, b = 1, 1
    for i in range(int((n-1)/2)):
        a = a + b
        b = a + b
    if n % 2 == 0:
        return b
    else:
        return a

def speedTesting(funcnum, n):
    res, microSec = 0, 0
    if funcnum == 1:
        start = datetime.now()
        res = fib01(n)
        end = datetime.now()
        microSec = int((end - start).total_seconds() * 1000000)
    if funcnum == 2:
        start = datetime.now()
        res = fib02(n)
        end = datetime.now()
        microSec = int((end - start).total_seconds() * 1000000)
    if funcnum == 3:
        start = datetime.now()
        res = fib03(n)
        end = datetime.now()
        microSec = int((end - start).total_seconds() * 1000000)
    return [res, microSec]

n = [10, 1000, 3000]
print("| {} | {} | {} | {} |".format("n", "Time consume 02", "Time consume 03", "Equal value"))
for i in n:
    # res01, ms01 = speedTesting(1, i)
    # res02, ms02 = speedTesting(2, i)
    # res03, ms03 = speedTesting(3, i)
    # print("| {} | {} | {} | {} |".format(ms01, ms02, ms03, (res01==res02) and (res01==res03)))

    res02, ms02 = speedTesting(2, i)
    res03, ms03 = speedTesting(3, i)
    print("| {} | {} | {} | {} |".format(i, ms02, ms03, res02==res03))