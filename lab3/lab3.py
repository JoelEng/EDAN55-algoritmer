import random
import copy
import matplotlib
from tqdm import tqdm
matplotlib.use('tkagg')

FILE = "data/pw09_100.9.txt"

edges, weights, vertices = [], {}, set()
f = open(FILE)
f.readline()
for x in open(FILE).readlines():
    tmp = x.split()
    if len(tmp) > 2:
        vertices.update([tmp[0], tmp[1]])
        edges.append((tmp[0], tmp[1]))
        weights[(tmp[0], tmp[1])] = tmp[2].strip()

vertices = list(vertices)


def checkCut(A, edges):
    counter = 0
    for v1, v2 in edges:
        if (v1 in A and v2 not in A) or (v2 in A and v1 not in A):
            counter += int(weights[(v1, v2)])
    return counter


def R(A):
    for vertex in vertices:
        if random.getrandbits(1):
            A.add(vertex)
    return checkCut(A, edges)


def S(A):
    maxDiff, currentMax, counter, failedSwaps = 0, 0, 0, 0
    while failedSwaps < len(vertices):
        nextVertice = vertices[counter % len(vertices)]
        counter += 1
        tmpA = copy.deepcopy(A)
        if nextVertice in tmpA:
            tmpA.remove(nextVertice)
        else:
            tmpA.add(nextVertice)

        testMax = checkCut(tmpA, edges)
        maxDiff = testMax-currentMax
        if maxDiff > 0:
            currentMax = testMax
            A = tmpA
            failedSwaps = 0
        else:
            failedSwaps += 1

    return currentMax


def RS(A):
    R(A)
    return S(A)


def run():
    valuesR, valuesS, valuesRS = [], [], []
    nbr = 100
    valuesS.append(S(set()))
    for _ in tqdm(range(nbr)):
        valuesR.append(R(set()))
        valuesRS.append(RS(set()))

    print("Avg R: " + str(sum(valuesR)/nbr))
    print("max cutsize for R: " + str(max(valuesR)))
    print("Avg S: " + str(sum(valuesS)/nbr))
    print("max cutsize for S: " + str(max(valuesS)))
    print("Avg RS: " + str(sum(valuesRS)/nbr))
    print("max cutsize for RS: " + str(max(valuesRS)))

    for v in valuesRS:
        print(v)


run()
