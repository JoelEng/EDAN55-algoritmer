
import random
import math

print("Hur många noder? ")
n = int(input())
markingTree = [False for _ in range(n)]
markCounter = 0


def getCounter():
    return markCounter


def getTree():
    return markingTree


def reset():
    global markingTree, markCounter
    markingTree = [False for _ in range(n)]
    markCounter = 0


def setTrue(i):
    global markingTree, markCounter
    if not markingTree[i]:
        markCounter += 1
        markingTree[i] = True


def randInteger(i, n):
    return random.randint(i, n-1)


def knuth():
    order = list(range(n))
    for i in range(n):
        r = randInteger(i, n)
        order[i], order[r] = order[r], order[i]
    return order


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
    if index * 2 + 1 >= n:
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


def iterateTree(index):
    for i in getNearby(index):
        if not markingTree[i]:
            if twoChildren(i) or siblingAndParent(i):
                setTrue(i)
                iterateTree(i)


def getNearby(index):
    if index == 0:
        return 1, 2
    nearby = []
    nearby.append(getParent(index))
    nearby.append(getSibling(index))
    if index * 2 + 1 < n:
        s1, s2 = getChildren(index)
        nearby.append(s1)
        nearby.append(s2)
    return nearby
