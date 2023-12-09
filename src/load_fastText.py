"""https://fasttext.cc/docs/en/aligned-vectors.html
"""

import io
import numpy as np

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    cnt = 0
    for line in fin:
        if cnt > 10:
            break
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
        cnt += 1
    return data

data = load_vectors("./data/wiki.en.align.vec")
print(data.keys())

print(list(data))