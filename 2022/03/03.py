"""
Advent of Code Day 01
Puzzle 01

Took me way too long and the solution is far away from being good
""" 

import string

letters = string.ascii_letters

backpacks = []
groups = []
with open('input.txt', 'r') as file:
    i = 0
    group = []
    for line in file:
        bp = line.strip()
        backpacks.append([bp[:len(bp) // 2], bp[len(bp) // 2:]])
        
        group.append(bp)
        #print(group)
        i += 1
        if i == 3:
            groups.append(group.copy())
            group.clear()
            i = 0


#print(backpacks)
#print(groups)

values = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

def puzzle1(backpacks):
    value = 0
    itemFound = False
    
    # not happy with that solution
    for bp in backpacks:
        for item in bp[0]:
            for item2 in bp[1]:
                if item == item2:
                    value += values.get(item)  # type: ignore
                    itemFound = True
                    break
            if itemFound:
                itemFound = False
                break
                
    return value
    
def puzzle2(groups):
    value = 0

    # unfortunately, I had to look that one up
    for (a, b, c) in groups:
        value += letters.index([x for x in a if x in b and x in c][0]) + 1

    
    return value

print(puzzle1(backpacks))
print(puzzle2(groups))