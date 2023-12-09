import re
import math

with open("day6.txt") as f:
    data = f.read().split("\n")

def f(times, distances):
    total = 1 
    for i in range(len(times)):
        t = times[i]
        d = distances[i]
        count = 0
        x1 = t/2 + math.sqrt((t/2)**2 - d)
        x2 = t/2 - math.sqrt((t/2)**2 - d)
        if x1 > x2:
            count = round(x1 -x2)
        else:
            count = round(x2 -x1)
        if count > 0:
            total *= count
    return total 

times, distances = [list(map(int, re.findall(r"(\d+)", line))) for line in data if line]
part1 = f(times, distances)

times, distances = [list(map(int, re.findall(r"(\d+)", line.replace(" ", "")))) for line in data if line]
part2 = f(times, distances)

print("Part1: ", part1)
print("Part2: ", part2)


