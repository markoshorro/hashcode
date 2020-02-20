#!/env/python3

import os
import re
import numpy as np
import pandas as pd

fname = "a_example.txt"


def read_input(fin):
    with open(fin) as f:
        B, L, D = [int(v) for v in f.readline().split(' ')]
        books = [int(v) for v in f.readline().split(' ')]
        toggle = True
        libraries = []
        p = []
        for l in f:
            if toggle:
                p.append([int(v) for v in l.split(' ')])
            else:
                p.append(sorted([int(v) for v in l.split(' ')], key=lambda i: books[i], reverse=True))
                libraries.append(p.copy())
                p.clear()
            toggle = not toggle
    return B, L, D, books, libraries

def value(libraries, nbooks):
    v = sum([books[i] for i in libraries[1][0:nbooks]])
    print(v)
    return v

def fitness(library, days):
    v = (value(library, days * library[0][2])/library[0][1])
    return v

if __name__ == '__main__':
    B, L, D, books, libraries = read_input(fname)
    print(books)
    libraries = sorted(libraries, key=lambda x: fitness(x, D))
    print(libraries)
    selected_libraries = []
    while D > 0 and len(libraries) > 0:
        D = D - libraries[-1][0][1]
        if D < 0:
            break
        l = libraries[-1]
        nbooks = D * l[0][2]
        l[1] = l[1][0:nbooks]
        selected_libraries.append(l)
        libraries = libraries[0:-1]
