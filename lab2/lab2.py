from pprint import pprint
from graph import graph
from itertools import chain, combinations

FILE = "eppstein"
ROOT = "1"


"Nodes is a dictionary on form {bagnbr : {{bag : {set of vertices} }, {children : {set of children}} {fu : {independent sets in bag}}}}"
graph, nodes = graph(FILE, ROOT).returnDicts()

def powerset(s):
    return [frozenset(t) for t in chain.from_iterable(combinations(s, r) for r in range(len(s)+1))]


def neighbours(ps):
    "Adjacent nodes, nodes that cannot be in the same independent set"
    neighbours = set()
    for s in ps:
        neighbours.update(graph[s])
    return neighbours


def checkIndependent(vertices):
    "Check if given set is an independent one"
    for vertex in vertices:
        if graph[vertex] & set(vertices):
            return False
    return True


def intersection(nodes, graphI):
    "Returns the intersection"
    intersect = [value for value in nodes if value in graphI]
    return intersect


def traverse(nodes, current=ROOT):
    ps = powerset(nodes[current]["bag"])
    ind_sets = frozenset([s for s in ps if checkIndependent(s)])
    if "children" not in nodes[current]:
        # current is a leaf node
        for s in ind_sets:
            nodes[current]["fu"][frozenset(s)] = len(s)
        return ind_sets

    # current is not a leaf node
    for child in nodes[current]["children"]:
        # traverse children before self
        children_ind_sets = traverse(nodes, child)
        ind_sets = (children_ind_sets | ind_sets)
        print("PSPS " + str(powerset(ind_sets)))

    independent_sets = [s for s in ind_sets if checkIndependent(s)]

    for s in independent_sets:
        nodes[current]["fu"][frozenset(s)] = len(s)
    return frozenset(independent_sets)


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
