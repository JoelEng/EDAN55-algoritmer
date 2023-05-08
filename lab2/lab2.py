from pprint import pprint
from graph import graph

FILE = "TutteGraph"
ROOT = "1"


"Nodes is a dictionary on form {bagnbr : {{bag : {set of vertices} }, {children : {set of children}} {fu : {independent sets in bag}}}}"
graph, nodes = graph(FILE, ROOT).returnDicts()


def powerset(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set:
            power_set = power_set+[list(sub_set)+[elem]]
    return power_set


def checkIndependent(vertices):
    "Check if given set is an independent one"
    # list(map(lambda s: str(s), vertices))
    for vertex in vertices:
        if set(graph[vertex]) & set(vertices):
            return False
    return True


def calc_ft(current, children, u):
    "(10.18)"
    ft = len(u)
    for child in children:
        max_value = 0
        for ui, fui in nodes[child]["fu"].items():
            if (set(ui) & set(nodes[current]["bag"])) == (set(u) & set(nodes[child]["bag"])):
                value = fui - len(u & ui)
                max_value = max(value, max_value)
                # new_set = frozenset.union(ui, u)
                # new_set = powerset(new_set)
                # nodes[current][]

        ft += max_value
    return ft


def traverse(nodes, current=ROOT):
    ps = powerset(nodes[current]["bag"])
    ind_sets = set([frozenset(u) for u in ps if checkIndependent(u)])

    if "children" not in nodes[current]:
        # current is a leaf node
        for u in ind_sets:
            nodes[current]["fu"][frozenset(u)] = len(u)
        return max(nodes[current]["fu"].values())

    for child in nodes[current]["children"]:
        traverse(nodes, child)  # traverse children before self

    for u in ind_sets:
        nodes[current]["fu"][u] = calc_ft(
            current, nodes[current]["children"], u)
    return max(nodes[current]["fu"].values())


res = traverse(nodes)
print("GRAPH:")
pprint(graph)
print("NODES:")
pprint(nodes)
print("max value: " + str(res))
