from pprint import pprint


class graph:
    def __init__(self, file, root):
        gr = open("./data/" + file + ".gr", "r").readlines()
        td = open("./data/"+file+".td", "r").readlines()
        self.G = dict()
        self.T = dict()
        self.nodes = dict()
        self.powersets = dict()

        for line in gr:
            line = line.strip()
            words = line.split(" ")
            if line[0] == "p":
                self.grVertices = words[2]
                self.grEdges = words[3]
            elif line[0] != "c":
                self.G.setdefault(words[0], set()).add(words[1])
                self.G.setdefault(words[1], set()).add(words[0])

        for line in td:
            line = line.strip()
            words = line.split(" ")
            if words[0] == "c":
                continue
            if words[0] == "s":
                self.bagsCount = words[2]
                self.treeWidth = int(words[3]) - 1
                self.tdVertices = words[4]
            elif words[0] == "b":
                self.nodes[words[1]] = dict()
                self.nodes[words[1]]["fu"] = dict()
                self.nodes[words[1]]["bag"] = words[2:len(words)]
            else:
                v0, v1 = words[0], words[1]
                self.T.setdefault(v0, set()).add(v1)
                self.T.setdefault(v1, set()).add(v0)
        self.makeTree(self.T, root)

    def returnDicts(self):
        return self.G, self.nodes

    def makeTree(self, graph, root):
        toSearch = set(root)
        done = set()
        tree = dict()

        while len(toSearch) > 0:
            current = toSearch.pop()
            for n in graph[current]:
                if n not in toSearch and n not in done:
                    tree.setdefault(current, set()).add(n)
                    toSearch.add(n)
            done.add(current)

        for key, val in tree.items():
            self.nodes[key]["children"] = val
