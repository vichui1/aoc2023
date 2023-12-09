from itertools import groupby
import re

with open("day7.txt") as f:
    data = f.read().split("\n")

data = [line.split(" ") for line in data if line]
sortedList = []
for hand, bet in data:
    sortedHand = "".join(sorted(hand))
    handStrength = sorted([len(''.join(g)) for _, g in groupby(sortedHand)], reverse = True)
    match handStrength:
        case [5]:
            sortedList.append(((hand, bet), 7))
        case [4,1]:
            sortedList.append(((hand, bet), 6))
        case [3,2]:
            sortedList.append(((hand, bet), 5))
        case [3,1,1]:
            sortedList.append(((hand, bet), 4))
        case [2,2,1]:
            sortedList.append(((hand, bet), 3))
        case [2,1,1,1]:
            sortedList.append(((hand, bet), 2))
        case [1,1,1,1,1]:
            sortedList.append(((hand, bet), 1))

sortedList = sorted(sortedList, key = lambda x: x[1])
customAlphabet = ['2','3','4','5','6','7','8','9','T','J', 'Q', 'K', 'A']

def sortCards(ls):
    temp = []
    for i in range(8):
        a = sorted([l for l in ls if l[1] == i], key=lambda hand: [customAlphabet.index(h) for h in hand[0][0]])
        temp += a
    return temp

total = 0
sortedList = sortCards(sortedList)
for i in range(0, len(sortedList)):
    bet = sortedList[i][0][1]
    total += int(bet) * (i+1)

part1 = total
print("Part 1: ", part1)
    
def jokerHand(hand):
    if not ('J' in hand):
        return hand
    else:
        sortedHand = "".join(sorted(hand))
        handStrength = sorted([(k, len(''.join(g))) for k, g in groupby(sortedHand)], reverse = True, key =lambda x: (x[1],customAlphabet.index(x[0])))
        print(handStrength)
        if len(handStrength) == 1:
            newRank = 'A'
        elif handStrength[0][0] == 'J':
            newRank = handStrength[1][0]
        else:
            newRank = handStrength[0][0]
        jHand = re.sub('J', newRank, hand)
        return jHand

sortedList = []
for hand, bet in data:
    jHand = jokerHand(hand)
    sortedHand = "".join(sorted(jHand))
    handStrength = sorted([len(''.join(g)) for _, g in groupby(sortedHand)], reverse = True)
    match handStrength:
        case [5]:
            sortedList.append(((hand, bet), 7))
        case [4,1]:
            sortedList.append(((hand, bet), 6))
        case [3,2]:
            sortedList.append(((hand, bet), 5))
        case [3,1,1]:
            sortedList.append(((hand, bet), 4))
        case [2,2,1]:
            sortedList.append(((hand, bet), 3))
        case [2,1,1,1]:
            sortedList.append(((hand, bet), 2))
        case [1,1,1,1,1]:
            sortedList.append(((hand, bet), 1))

sortedList = sorted(sortedList, key = lambda x: x[1])
customAlphabet2 = ['J','2','3','4','5','6','7','8','9','T', 'Q', 'K', 'A']

def sortCards2(ls):
    temp = []
    for i in range(8):
        a = sorted([l for l in ls if l[1] == i], key=lambda hand: [customAlphabet2.index(h) for h in hand[0][0]])
        temp += a
    return temp

total = 0
sortedList = sortCards2(sortedList)
for i in range(0, len(sortedList)):
    bet = sortedList[i][0][1]
    total += int(bet) * (i+1)

part2 = total
print("Part 2: ", part2)