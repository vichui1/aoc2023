import re
from collections import defaultdict
with open("day4.txt") as f:
    data = f.read().splitlines()

ns = [re.sub(r'Card\s*\d+:', '', l) for l in data]
ss = [n.split("|") for n in ns]

t1 = 0
c = defaultdict(int)
for i, s in enumerate(ss):
    c[i] += 1
    s1 = set(re.findall(r'\d+', s[0]))
    s2 = set(re.findall(r'\d+', s[1]))
    wn = len(s1 & s2)
    if wn > 0:
        t1 += 2**(wn -1)
    for j in range(wn):
        c[i+1+j] += c[i]

part1 = t1
part2 = sum(c.values())

print("Part 1: ", part1)
print("Part 2: ", part2)
