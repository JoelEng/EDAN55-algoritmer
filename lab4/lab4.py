from pprint import pprint
import random

FILE = "toy"

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

pprint(edges)


def chooseRoad(start):
    "Returns a (weighted) randomly chosen road from start"
    probs = []
    ends = []
    for e, d in edges[start].items():
        ends.append(e)
        probs.append(d["prob"])

    return random.choices(ends, weights=probs)[0]


def monteCarlo(start):
    current = start
    road = [start]
    time = 0
    while current != H:
        new = chooseRoad(current)
        road.append(new)
        time += edges[current][new]["time"]
        current = new
    return time, road


time, road = monteCarlo(F)
print("Time: " + str(time) + " minutes")
pprint("Road: " + str(road))
