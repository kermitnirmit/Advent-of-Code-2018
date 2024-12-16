from utils import ints, edit_distance
from collections import  Counter, defaultdict
f = [x for x in open("input.txt").read().strip().splitlines()]
c_map = defaultdict(int)
c_id_to_square = defaultdict(set)
for line in f:
    c_id, j, i, w, h = ints(line)
    print(c_id, j, i, w, h)

    for ni in range(i, i + h ):
        for nj in range(j, j + w ):
            c_map[(ni,nj)] += 1
            c_id_to_square[c_id].add((ni,nj))
p1 = 0
for k,v in c_map.items():
    if v > 1:
        p1 += 1
print(p1)
for k,v in c_id_to_square.items():
    if all(c_map[x] == 1 for x in v):
        print(k)
        break
