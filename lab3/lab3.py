from pprint import pprint
import random




file = "data\matching_1000.txt"
vertices, weights = [], {}
f = open(file)
f.readline()
for x in open(file).readlines():
    tmp = x.split(" ")
    if len(tmp) > 2:
        vertices.append((tmp[0],tmp[1]))
        weights[(tmp[0],tmp[1])] = tmp[2].strip()

A = {}

def assign(vertex):
    if random.randint(0, 1) == 1:
        A.append(vertex)
