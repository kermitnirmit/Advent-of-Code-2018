from utils import ints, edit_distance
from collections import  Counter, defaultdict
f = [x for x in open("input.txt").read().strip().splitlines()]

twos, threes = 0, 0
for line in f:
    c = Counter(line)
    rev_map = defaultdict(int)
    for k,v in c.items():
        if v == 2:
            twos += 1
            break
    for k,v in c.items():
        if v == 3:
            threes += 1
            break
print(twos * threes)

for i, line in enumerate(f):
    for j, line_2 in enumerate(f):
        if i != j:
            if edit_distance(line, line_2) == 1:
                print(line, line_2)
                ret = ""
                for a,b in zip(line, line_2):
                    if a == b:
                       ret += a
                print(ret)
                break