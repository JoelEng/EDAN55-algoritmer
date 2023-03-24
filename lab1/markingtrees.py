
import random
import math

print("Hur många noder? ")
n = int(input())
markingTree = [False for _ in range(n)]


def reset():
    global markingTree
    markingTree = [False for _ in range(n)]


def randInteger(i, n):
    return random.randint(i, n-1)


def R1():
    count = 0
    while True:
        count += 1
        nextColor = randInteger(0, n)
        markingTree[int(nextColor)] = True
        iterateTree()
        if all(markingTree):
            return count


def knuth():
    order = list(range(n))
    for i in range(n):
        r = randInteger(i, n)
        order[i], order[r] = order[r], order[i]
    return order


def R2():
    count = 0
    order = knuth()
    for i in order:
        count += 1
        markingTree[i] = True
        iterateTree()
        if all(markingTree):
            break
    return count


def R3():
    count = 0
    order = knuth()
    for i in order:
        if markingTree[i]:
            continue
        count += 1
        markingTree[i] = True
        iterateTree()
        if all(markingTree):
            break
    return count


def getChildren(index: int):
    left = 2 * index + 1
    right = 2 * index + 2
    return left, right


def getParent(index: int):
    return math.ceil((index / 2) - 1)


def getSibling(index: int):
    if index % 2 == 0:
        return index - 1
    else:
        return index + 1


def twoChildren(index: int):
    "rule 1"
    if index * 2 + 1 >= len(markingTree):
        return False
    left, right = getChildren(index)
    return markingTree[left] and markingTree[right]


def siblingAndParent(index: int):
    "rule 2"
    if index == 0:
        return False
    parent = getParent(index)
    sibling = getSibling(index)
    return markingTree[parent] and markingTree[sibling]


def iterateTree():
    keepOnGoing = True

    while keepOnGoing:
        keepOnGoing = False
        for i, val in enumerate(markingTree):
            if not val:
                mark = twoChildren(i) or siblingAndParent(i)
                if mark:
                    markingTree[i] = True
                    keepOnGoing = True


reset()
print("R1 iterated: " + str(R1()))

reset()
print("R2 iterated: " + str(R2()))

reset()
print("R3 iterated: " + str(R3()))
