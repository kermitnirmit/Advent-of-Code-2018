import parse
from collections import  defaultdict
from utils import topological_sort
f = [x for x in open("input.txt").read().strip().splitlines()]

adj_list = defaultdict(list)
import re
for line in f:
    before, after = re.findall(r"Step ([A-Z]) must be finished before step ([A-Z])", line)[0]
    print(before, after)
    # adj_list[after].append(before)
    adj_list[before].append(after)

print(adj_list)


print("".join(topological_sort(adj_list)))