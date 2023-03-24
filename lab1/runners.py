from markingtrees import *
import statistics


def R1():
    count = 0
    while getCounter() < n:
        count += 1
        i = randInteger(0, n)
        setTrue(i)
        iterateTree(i)
    return count


def R2():
    count = 0
    order = knuth()
    for i in order:
        count += 1
        setTrue(i)
        iterateTree(i)
        if getCounter() == n:
            break
    return count


def R3():
    count = 0
    order = knuth()
    for i in order:
        if getTree()[i]:
            continue
        count += 1
        setTrue(i)
        iterateTree(i)
        if getCounter() == n:
            break
    return count


res1 = []
res2 = []
res3 = []

for i in range(15):
    print(f"Iteration {str(i)}")
    reset()
    result1 = R1()
    res1.append(result1)
    print("R1 iterated: " + str(result1))

    reset()
    result2 = R2()
    res2.append(result2)
    print("R2 iterated: " + str(result2))

    reset()
    result3 = R3()
    res3.append(result3)
    print("R3 iterated: " + str(result3))

print(f"\nn: {n}")
for idx, res in enumerate([res1, res2, res3]):
    print(f"R{idx+1} Mean:\t{str(statistics.mean(res))}")
    print(f"R{idx+1} Std dev:\t{str(statistics.stdev(res))}")
