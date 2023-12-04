import re

with open("day2.txt") as f:
    data = f.read().strip()

ls = data.split("\n")
gs = [l.replace(";", ",").split(",") for l in ls]

def colorInSet(s, c):
    if c in s:
        return True
    else:
        return False

def validSet(s):
    cubes = int(re.findall("\d+", s)[-1])
    if colorInSet(s,"red"):
        if cubes > 12: return False
    if colorInSet(s,"green"):
        if cubes > 13: return False
    if colorInSet(s,"blue"):
        if cubes > 14: return False
    return True

validIds = []
for i in range(1,len(gs)+1):
    g = gs[i-1]
    if all(map(validSet, g)):
        validIds.append(i)

part1 = sum(validIds)

def maxCubes(rgb, s):
    cubes = int(re.findall("\d+", s)[-1])
    if colorInSet(s,"red"):
        if cubes > rgb[0]: rgb[0] = cubes
    if colorInSet(s,"green"):
        if cubes > rgb[1]: rgb[1] = cubes
    if colorInSet(s,"blue"):
        if cubes > rgb[2]: rgb[2] = cubes
    return rgb

powerSum = 0
for g in gs:
    rgb = [1,1,1]
    for s in g:
        rgb = maxCubes(rgb, s)
    power = rgb[0] * rgb[1] * rgb [2]
    powerSum += power

part2 = powerSum
print("Part1: ", part1)
print("Part2: ", part2)