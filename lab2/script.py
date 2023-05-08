from os import listdir
from os.path import isfile, join
from lab2 import run
import multiprocessing
import time

PATH = "data"


def runFile():
    if suffix == "gr":
        try:
            run(name)
        except Exception:
            print(f"{name} & & FAILED & \\\\")


if __name__ == '__main__':
    files = [f for f in listdir(PATH) if isfile(join(PATH, f))]

    for file in files:
        name, suffix = file.split(".")
        p = multiprocessing.Process(target=runFile)
        p.start()

        p.join(60)

        if p.is_alive():
            print(f"{name} & & TOO SLOW & \\\\")
            p.terminate()
            p.join()
