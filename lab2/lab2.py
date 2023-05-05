from pprint import pprint
from graph import graph
from itertools import chain, combinations


# En funktion som traversar
# En funktion som beräknar
#

FILE = "eppstein"
ROOT = "1"


"Nodes is a dictionary on form {bagnbr : {{bag : {set of vertices} }, {children : {set of children}} {fu : {independent sets in bag}}}}"
graph, nodes = graph(FILE, ROOT).returnDicts()


def powerse1t(s):
    return [tuple(t) for t in chain.from_iterable(combinations(s, r) for r in range(len(s)+1))]


def powerset(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set:
            power_set = power_set+[list(sub_set)+[elem]]
    return power_set


# def neighbours(ps):
#     "Adjacent nodes, nodes that cannot be in the same independent set"
#     neighbours = set()
#     for s in ps:
#         neighbours.update(graph[s])
#     return neighbours


def checkIndependent(vertices):
    "Check if given set is an independent one"
    # list(map(lambda s: str(s), vertices))
    for vertex in vertices:
        if graph[vertex] & set(vertices):
            return False
    return True


# def intersection(nodes, graphI):
#     "Returns the intersection"
#     intersect = [value for value in nodes if value in graphI]
#     return intersect

def calc_ft(independent_set, children):
    "(10.18)"
    ft = len(independent_set)
    for child in children:
        max_value = 0
        for key, val in nodes[child]["fu"].items():
            calc_ft(key, nodes[child]["children"])
            value = nodes[child]["fu"][val] - len(independent_set & key)
            max_value = max(value, max_value)
        ft += max_value
    return ft


def traverse(nodes, current=ROOT):
    ps = powerset(nodes[current]["bag"])
    ind_sets = set([s for s in ps if checkIndependent(s)])
    if "children" not in nodes[current]:
        # current is a leaf node
        for s in ind_sets:
            nodes[current]["fu"][tuple(s)] = len(s)
        return

    # current is not a leaf node
    for child in nodes[current]["children"]:
        # traverse children before self
        traverse(nodes, child)
        # pprint(ind_sets)

    for s in ind_sets:
        nodes[current]["fu"][frozenset(s)] = len(s)


traverse(nodes)

print("GRAPH:")
pprint(graph)
print("NODES:")
pprint(nodes)

pprint("")


# for name, vertices in bags.items():
#     ps = powerset(vertices)
#     max_val = 0
#     independent_sets[name] = set()
#     for s in ps:
#         if checkIndependent(s, graph):
#             independent_sets[name].add(s)
#             max_val = max(max_val, len(s))
#     weights[name] = max_val


# print("All independent sets")
# pprint(independent_sets)

# print("Leaf nodes")

# for leaf in leaf_nodes_list:
#     for s in independent_sets[leaf]:
#         if not leaf in calculations:
#             calculations[leaf] = {s: len(s)}
#         else:
#             calculations[leaf].update({s: len(s)})


# def calculate(tree, ui, w, inde_set={}):
#     # base-case: rotnoden
#     if ui in leaf_nodes_list:
#         return calculations[ui]

#     for child in tree[ui]:
#         temp_set = inde_set.append(child)
#         if checkIndependent(temp_set):
#             return calculate(tree, child, len(temp_set), temp_set)


# print("Calc")
# pprint(calculations)
