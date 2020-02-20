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
        idl = 0
        toggle = True
        libraries = []
        p = []
        for l in f:
            if toggle:
                p.append([int(v) for v in l.split(' ')] + [idl])
            else:
                p.append(sorted([int(v) for v in l.split(' ')], key=lambda i: books[i], reverse=True))
                libraries.append(p.copy())
                p.clear()
                idl = idl + 1
            toggle = not toggle
    return B, L, D, books, libraries

def value(libraries, nbooks):
    v = sum([books[i] for i in libraries[1][0:nbooks]])
    print(v)
    return v

def fitness(library, days):
    v = (value(library, days * library[0][2])/library[0][1])
    return v

def create_sim_matrix(books, libraries):
    matrix = np.zeros((len(libraries), len(libraries)))
    for i in range(len(libraries)):
        for j in range(len(libraries)):
            v = sum([books[b] for b in list(set.intersection(set(libraries[i][1]), set(libraries[j][1])))])
            matrix[i][j] = v
            matrix[j][i] = v
    print(matrix)
    return matrix


if __name__ == '__main__':

    B, L, D, books, libraries = read_input(fname)
    libraries = sorted(libraries, key=lambda x: fitness(x, D))
    create_sim_matrix(books, libraries)
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
