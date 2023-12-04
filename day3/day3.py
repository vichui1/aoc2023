import re
import itertools

with open("day3.txt") as f:
    data = f.read().split("\n")

m = [list(row) for row in data if row]

# add sentinel rows
for r in m:
    r.insert(0,".")
    r.append(".")

fill = ["."]*len(m[0])
m.insert(0, fill)
m.append(fill)

def checkSurrounding(r,c):
   sur = [m[r-1][c-1],
    m[r-1][c],
    m[r-1][c+1],
    m[r][c-1],
    m[r][c+1],
    m[r+1][c-1],
    m[r+1][c],
    m[r+1][c+1]]
   
   if any(map(checkSymbol, sur)):
       return True
   else: return False
       
def checkSymbol(s):
    if not s.isalnum() and s != ".":
        return True
    else: return False

def removeFromMatrix(ls):
    for l in ls:
        r,c = l
        m[r][c] = "."
    remove.clear()

remove = []
for r in range(1, len(m) - 1):
    for c in range(1, len(m[0]) - 1):
        char = m[r][c]
        if char.isdigit():
            if not checkSurrounding(r,c):
                remove.append((r,c))
                prevChar = m[r][c-1]
                if (len(remove) == 1 and prevChar.isdigit()):
                    remove.clear()
            else: remove.clear()
        else:
            removeFromMatrix(remove)
    removeFromMatrix(remove)

ls = ["".join(r) for r in m]
ns = [re.findall(r'(\d+)', x) for x in ls]
flat_ns = list(itertools.chain(*ns))
part1 = sum(int(n) for n in flat_ns)

def neighbourNums(r,c):
    ls = []
    for i in range(r-1, r+2):
        for j in range(c-1,c+2):
            if i == r and j ==c:
                continue
            elif m[i][j].isdigit():
                if j == c-1:
                    ls.append((i,j))
                else:
                    if not m[i][j-1].isdigit():
                        ls.append((i,j))
    return ls


def getNum(pair):
    r, c = pair
    num = m[r][c]
    while True:
        c += 1
        next = m[r][c]
        if next.isdigit():
            num += next
        else: break
    r, c = pair
    while True:
        c -= 1
        prev = m[r][c]
        if prev.isdigit():
            num = prev + num
        else: break
    return int(num)

part2 = 0
for r in range(1, len(m) - 1):
    for c in range(1, len(m[0]) - 1):
        char = m[r][c]
        if char == "*":
            ns = neighbourNums(r,c)
            if len(ns) == 2:
                n1 = getNum(ns[0])
                n2 = getNum(ns[1])
                part2 += n1*n2
            
print("Part1: ", part1)
print("Part2: ", part2)

