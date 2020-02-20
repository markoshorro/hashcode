#!/env/python3

import os
import re
import numpy as np
import pandas as pd

fname = ["a_example.txt"]


def read_input(fin):
    with open(fin) as f:
        B, L, D = [int(v) for v in f.readline().split(' ')]
        books = [int(v) for v in f.readline().split(' ')]
        idl = 0
        toggle = True
        libraries = []
        p = []
        for l in f:
            if l == "\n":
                continue
            if toggle:
                p.append([int(v) for v in l.split(' ')] + [idl])
            else:
                p.append(sorted([int(v) for v in l.split(' ')],
                                key=lambda i: books[i], reverse=True))
                libraries.append(p.copy())
                p.clear()
                idl = idl + 1
            toggle = not toggle
    return B, L, D, books, libraries


def sum_not_0(books, lbooks, nbooks):
    s = 0
    selection = []
    i = 0
    while len(selection) < nbooks and i < len(lbooks):
        val = books[lbooks[i]]
        if val > 0:
            s += val
            selection.append(lbooks[i])
        i += 1
    return s, selection

def value(books, library, nbooks):
    return sum_not_0(books, library[1], nbooks)[0]

def fitness(books, library, days):
    return value(books, library, days * library[0][2]) * library[0][2]/library[0][1]

def create_sim_matrix(books, libraries):
    matrix = np.zeros((len(libraries), len(libraries)))
    for i in range(len(libraries)):
        for j in range(len(libraries)):
            v = sum([books[b] for b in list(set.intersection(set(libraries[i][1]), set(libraries[j][1])))])
            matrix[i][j] = v
            matrix[j][i] = v
    return matrix


if __name__ == '__main__':
    for inputfile in fname:
        B, L, D, books, libraries = read_input(inputfile)
        libraries = sorted(libraries, key=lambda x: fitness(books, x, D), reverse=True)
        current_fitness = np.array([fitness(books, x, D) for x in libraries])
        selected_libraries = []
        while D > 0 and len(libraries) > 0:
            pos = np.argmax(current_fitness)
            l = libraries[pos]
            D = D - l[0][1]
            if D < 0:
                break
            nbooks = D * l[0][2]
            l[1] = sum_not_0(books, l[1], nbooks)[1]
            selected_libraries.append(l.copy())
            for b in l[1]:
                books[b] = 0
            current_fitness = np.array([fitness(books, x, D) for x in libraries])

        with open(inputfile.split(".txt")[0] + ".out", "w") as f:
            f.write(str(len(selected_libraries)) + "\n")
            for library in selected_libraries:
                f.write(str(library[0][-1]) + " " + str(len(library[1])) + "\n")
                for book in library[1]:
                    f.write(str(book) + " ")
                f.write("\n")
