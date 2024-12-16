from collections import defaultdict

from utils import ints

f = [x for x in open("input.txt").read().strip().splitlines()]

q = []
for line in f:
    vals = ints(line)
    vals = [abs(x) for x in vals]
    i = 0
    action = 0
    if len(vals) == 6:
        y,mo,d,h,m,i = vals
        action = 1
    else:
        y,mo,d,h,m = vals
        action = 1 if line[-2:] == "up" else 0
    q.append((y,mo,d,h,m, i, action, line))

q.sort()


n_q = []
for y,mo,d,h,m, i, action, line in q:
    if i == 0:
        i = n_q[-1][5]
    n_q.append((y,mo,d,h,m, i, action, line))
ids_to_gd_counters = defaultdict(dict)
# n_q = n_q[:3]
for l, l2 in zip(n_q, n_q[1:]):
    y, mo, day, _, m, i, action, l_text = l
    y_2, mo_2, day_2, _, m2, i2, action2, l2_text = l2
    if i != i2:
        m2 = 59
    if (y, mo, day) < (y_2, mo_2, day_2):
        m = m - 60

    if i not in ids_to_gd_counters:
        ids_to_gd_counters[i] = defaultdict(int)
    for t in range(m, m2):
        if not action:
            ids_to_gd_counters[i][t % 60] += 1

max_id = max(ids_to_gd_counters, key=lambda x: sum(ids_to_gd_counters[x].values()))
max_id_counter = max(ids_to_gd_counters[max_id], key=lambda x: ids_to_gd_counters[max_id][x])
print(max_id * max_id_counter)


max_min = -1
max_times = -1
guard_with_max = -1
for guard, min_to_times_d in ids_to_gd_counters.items():
    for minute, times in min_to_times_d.items():
        if times > max_times:
            max_times = times
            max_min = minute
            guard_with_max = guard
print(guard_with_max * max_min)
