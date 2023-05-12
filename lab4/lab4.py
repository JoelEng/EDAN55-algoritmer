from pprint import pprint
import random
import numpy as np
import time as t

FILE = "strange2"

f = open(f"./data/{FILE}.in")
N, M, H, F, P = f.readline().split()

"from_node: {to_node: (time, prob)}"
edges = dict()
for line in f.readlines():
    u, v, time, p_uv, p_vu = line.split()
    edges.setdefault(u, dict()).update(
        {v: {"time": int(time), "prob": float(p_uv)}})
    edges.setdefault(v, dict()).update(
        {u: {"time": int(time), "prob": float(p_vu)}})


def areConnected(n1, n2):
    visited = set()
    toVisit = set(n1)
    while len(toVisit) != 0:
        current = toVisit.pop()
        for neighbour in edges[current].keys():
            if neighbour not in visited:
                toVisit.add(neighbour)
        visited.add(current)
    return n2 in visited


# MONTE CARLO ----------------------------------------

def chooseRoad(start):
    "Returns a (weighted) randomly chosen road from start"
    probs = []
    ends = []
    for e, d in edges[start].items():
        ends.append(e)
        probs.append(d["prob"])

    return random.choices(ends, weights=probs)[0]


def randomPath(start):
    current = start
    road = [start]
    time = 0
    while current != H:
        new = chooseRoad(current)
        road.append(new)
        time += edges[current][new]["time"]
        current = new
    return time


def monteCarloAverage(start, count):
    times = []
    for _ in range(count):
        time = randomPath(start)
        times.append(time)
    return sum(times)/count


def monteCarlo():
    startTime = t.time()
    runs = 10000

    if areConnected(F, H):
        averageF = monteCarloAverage(F, runs)
        print(f"MC F: {averageF} minutes")
        # value = (233.69047619 - averageF)/233.69047619
        # print("accuracy for F: " + str(value))
    else:
        print("We tried to deliver your package, but you were not at home. MVH FedUps")

    if areConnected(P, H):
        averageP = monteCarloAverage(P, runs)
        print(f"MC P: {averageP} minutes")
        # value = (233.333333333 - averageP)/233.333333333
        # print("accuracy for P: " + str(value))
    else:
        print("We tried to deliver your package, but you were not at home. MVH PostNHL")

    return t.time() - startTime


# MARKOV ------------------------------------------

def expectedTime(node):
    times = []
    for d2 in edges[node].values():
        times.append(d2["time"]*d2["prob"])
    return sum(times)


def markov():
    A = np.zeros((int(N), int(N)))
    b = np.zeros(int(N))
    I = np.identity(int(N))

    for u, d in edges.items():
        for v, d2 in d.items():
            A[int(u), int(v)] = d2["prob"]
        b[int(u)] = expectedTime(u)
    try:
        solution = np.linalg.solve(A - I, -b)
        print(f"Markov F: {solution[int(F)]}")
        print(f"Markov P: {solution[int(P)]}")
    except Exception:
        print(
            "We tried to deliver your package, but you were not at home. xoxo Andrey Markov")


# BENCHMARKING --------------------------------------


# print(monteCarlo())
markov()
