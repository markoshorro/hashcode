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
                p.append([int(v) for v in l.split(' ')])
                libraries.append(p.copy())
                p.clear()
            toggle = not toggle
    return B, L, D, books, libraries