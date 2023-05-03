from pprint import pprint
from graph import graph
from itertools import chain, combinations

ROOT = "1"

adjacent_nodes = {}
bags = {}
independent_sets = {}
leaf_nodes_list = []
calculations = dict(dict())


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def leaf_nodes(tree, node="1"):
    if node not in tree:
        leaf_nodes_list.append(node)
    for child in tree[node]:
        leaf_nodes(tree, child)


def neighbours(ps):
    neighbours = set()
    for s in ps:
        neighbours.update(graph[s])
    return neighbours


def checkIndependent(name, nodes, graphI):
    for node in nodes:
        if graphI[node] & set(nodes):
            return False
    independent_sets[name].add(nodes)
    return True


def intersection(nodes, graphI):
    intersect = [value for value in nodes if value in graphI]
    return intersect


graph = graph("eppstein.gr", "eppstein.td")
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
    independent_sets[name] = set()
    for s in ps:
        if checkIndependent(name, s, graph):
            max_val = max(max_val, len(s))
    weights[name] = max_val

print("All independent sets")
pprint(independent_sets)

print("Leaf nodes")
leaf_nodes(tdGraph)
pprint(leaf_nodes_list)

for leaf in leaf_nodes_list:
    for s in independent_sets[leaf]:
        if not leaf in calculations:
            calculations[leaf] = {s: len(s)}
        else:
            calculations[leaf].update({s: len(s)})


def calculate(tree, ui, w, inde_set={}):
    # base-case: rotnoden
    if ui in leaf_nodes_list:
        return calculations[ui]

    for child in tree[ui]:
        temp_set = inde_set.append(child)
        if checkIndependent(temp_set):
            return calculate(tree, child, len(temp_set), temp_set)

    #
    #
    #


print("Calc")
pprint(calculations)
