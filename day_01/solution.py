from utils import ints
f = [x for x in open("input.txt").read().strip().splitlines()]
c = 0
seen = set()
seen.add(0)
i = 0
p1 = False
for i in range(1000000):
    ind = i % len(f)

    line = f[ind]
    c += ints(line)[0]
    if not p1 and ind == len(f) - 1:
        print(c)
        p1 = True
    # print(c)
    if c in seen:
        print(c)
        break
    else:
        seen.add(c)