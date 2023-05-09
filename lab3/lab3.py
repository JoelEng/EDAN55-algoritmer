from pprint import pprint
import random

filename = "pw09_100.9"
content = open("./data/" + filename + ".txt", "r").readlines()


A = {}
B = {}

def assign(vertex):
    if random.randint(0, 1) == 1:
        A.append(vertex)
