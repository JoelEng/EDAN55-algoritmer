from markingtrees import *


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


reset()
print("R1 iterated: " + str(R1()))

reset()
print("R2 iterated: " + str(R2()))

reset()
print("R3 iterated: " + str(R3()))
