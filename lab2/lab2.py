from pprint import pprint
from graph import graph
from itertools import chain, combinations


adjacent_nodes = {}
bags = {}
independent_sets = {}


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def checkIndependent(nodes, graphI):
    for node in nodes:
        if graphI[node] & set(nodes):
            print("False")
            return False
    print("True")
    independent_sets[nodes] = len(nodes)
    return True

# def intersection(nodes, graphI):
#    intersect = [value for value in nodes if value in graphI]
#    return intersect


graph = graph("web4.gr", "web4.td")
graph, tdGraph, bags = graph.returnDicts()
print("GRAPH:")
pprint(graph)
print("TD GRAPH:")
pprint(tdGraph)
print("BAGS:")
pprint(bags)

weights = dict()

for name, vertices in bags.items():
    ps = powerset(vertices)
    max_val = 0

    for s in ps:
        if checkIndependent(s, graph):
            max_val = max(max_val, len(s))
    weights[name] = max_val

print("Max independent sets")
print(weights)
pprint(independent_sets)
