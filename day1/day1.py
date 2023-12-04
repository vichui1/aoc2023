with open("day1.txt") as f:
    data = f.readlines()

def calibration(data):
    digits = [[int(i) for i in str if i.isdigit()] for str in data]
    twoDigits = [ds[::len(ds)-1] if len(ds) >= 2 else ds+ds for ds in digits]
    concatDigits = [int("".join([str(d) for d in ds])) for ds in twoDigits if ds]
    return concatDigits

part1 = sum(calibration(data))

n1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
n2 = ["1one", "2two", "3three", "4four", "5five", "6six", "7seven", "8eight", "9nine"]
numDict = dict(zip(n1, n2))

def convStr(s):
    word = ""
    for c in s:
        word += c
        for n in n1:
            if n in word:
                s = s.replace(n, str(numDict[n]))  
    return s

cs = [convStr(l) for l in data]
part2 = sum(calibration(cs))

print("Part1: ", part1)
print("Part2: ", part2)