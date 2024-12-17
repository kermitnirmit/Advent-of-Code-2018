from utils import ints
from collections import Counter

f = [x for x in  open("input.txt", "r").read().strip().split("\n")]

points = set()
for line in f:
    x,y,dx,dy = ints(line)
    points.add((x,y, dx, dy))

print(points)

def print_points(points, filename):
    min_x = min(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_x = max(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda x: x[1])[1]
    just_coords = set((x,y) for x,y,dx,dy in points)
    # print(min_x, min_y, max_x, max_y)
    
    with open(f"output_{filename}.txt", "w") as f:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in just_coords:
                    f.write("#")
                else:
                    f.write(".")
            f.write("\n")


# print_points(points)

for i in range(100000):
    n_points = set()
    for (x,y,dx,dy) in points:
        x += dx
        y += dy
        n_points.add((x,y, dx, dy))
    points = n_points
    # find 5 points with the same x value and consecutive y values
    x_values = [x for x,y,dx,dy in points]
    x_values = Counter(x_values)
    printed_line = False
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]
    if max_y - min_y <= 10: 
        for x in x_values:
            if x_values[x] >= 10 and not printed_line:
                # print(x)
                print(f"p2 answer: {i + 1}")
                print_points(points, i + 1)
                print(f"Check the output file named output_{i + 1}.txt")
                break


# print(points)
