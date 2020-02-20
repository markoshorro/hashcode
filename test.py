#!/env/python3

import os
import re
import numpy as np
import pandas as pd

file = "file"

with open(file) as f:
    for l in f:
        # read line
