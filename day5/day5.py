import re

with open("day5.txt") as f:
    data = f.read().split("\n\n")

seeds = re.findall("\d+",data[0])
seeds = [int(s) for s in seeds]
rest = data[1:]

alm = [line.split("\n") for line in rest]
alm = [[re.findall("\d+", "".join(a)) for a in ax if bool(re.search("\d+",a))] for ax in alm]

def getDestination(num, maps):
    for m in maps:
        res = checkMap(int(m[0]),int(m[1]),int(m[2]), num)
        if res == num:
            continue
        else: break
    return res

def checkMap(d, s, r, num):
    if num >= s and num < (s + r):
        newDestination = num - s + d 
        return newDestination
    return num

locations = []

for s in seeds:
    for a in alm:
        s = getDestination(s,a)
    locations.append(s)

locations2 = []
newSeeds = []

def getDestinationRanges(ranges, maps):
    newDestRanges = []
    seedRanges = ranges

    while seedRanges:
        start, end = seedRanges.pop()
        for m in maps:
            d = int(m[0])
            s = int(m[1])
            r = int(m[2])

            overlap_start = max(start, s)
            overlap_end = min(end, s + r)
            if overlap_start < overlap_end:
                newDestRanges.append((overlap_start - s + d, overlap_end - s + d))
                if overlap_start > start:
                    seedRanges.append((start, overlap_start))
                if end > overlap_end:
                    seedRanges.append((overlap_end, end))
                break
        else:
            newDestRanges.append((start, end))
    return newDestRanges

for i in range(0,len(seeds),2):
    s1 = seeds[i]
    s2 = seeds[i+1]
    newSeeds.append((s1,s1 + s2))

locationRanges = []
for s in newSeeds:
    drs = [s]
    for maps in alm:
        drs = getDestinationRanges(drs,maps)
    locationRanges = locationRanges + drs

part1 = min(locations)
part2 = min(locationRanges)[0]

print("Part1: ", part1)
print("Part2: ", part2)