from collections import defaultdict

import numpy as np

from utils import ints

f = [x for x in open("input.txt").read().strip().splitlines()]
points = []
for line in f:
    a, b = ints(line)
    points.append((a, b))
points = np.array(points)

# Find bounding box of points
min_x = min(points[:, 0])
max_x = max(points[:, 0])
min_y = min(points[:, 1])
max_y = max(points[:, 1])

# Create grid of points to check
x_range = range(int(min_x) - 1, int(max_x) + 2)
y_range = range(int(min_y) - 1, int(max_y) + 2)

# Count points closest to each input point and track which ones are infinite
area_counts = defaultdict(int)
infinite_points = set()

# Check boundary points to identify infinite regions
for x in x_range:
    for y in [min_y - 1, max_y + 1]:  # Top and bottom edges
        min_dist = float('inf')
        closest_idx = None
        for i, point in enumerate(points):
            dist = abs(x - point[0]) + abs(y - point[1])
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
            elif dist == min_dist:
                closest_idx = None
        if closest_idx is not None:
            infinite_points.add(closest_idx)

for x in [min_x - 1, max_x + 1]:  # Left and right edges
    for y in y_range:
        min_dist = float('inf')
        closest_idx = None
        for i, point in enumerate(points):
            dist = abs(x - point[0]) + abs(y - point[1])
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
            elif dist == min_dist:
                closest_idx = None
        if closest_idx is not None:
            infinite_points.add(closest_idx)

# Count areas for all points
for x in x_range:
    for y in y_range:
        min_dist = float('inf')
        closest_idx = None
        for i, point in enumerate(points):
            dist = abs(x - point[0]) + abs(y - point[1])
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
            elif dist == min_dist:
                closest_idx = None
        if closest_idx is not None:
            area_counts[closest_idx] += 1

# Filter out infinite areas
finite_areas = {idx: count for idx, count in area_counts.items()
                if idx not in infinite_points}

print(max(finite_areas.values()))


def part2(points, limit=10000):
    # Find bounding box
    # min_x = min(points[:, 0])
    # max_x = max(points[:, 0])
    # min_y = min(points[:, 1])
    # max_y = max(points[:, 1])

    # Expand search space - the region might extend beyond the input points
    margin = limit // len(points)  # rough estimate of how far to look
    count = 0

    for x in range(min_x - margin, max_x + margin):
        for y in range(min_y - margin, max_y + margin):
            total_distance = sum(abs(x - p[0]) + abs(y - p[1]) for p in points)
            if total_distance < limit:
                count += 1

    return count


print(part2(points))
