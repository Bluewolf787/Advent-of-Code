
stra = ()
with open('input.txt', 'r') as file:
    for line in file:
        stra += (line.strip().replace(' ', ''),)

#print(stra)


# 0 for lose
# 3 for draw
# 6 for win

# 1 for rock
# 2 for paper
# 3 for scissors

# rock: A;X
# paper: B;Y
# scissors: C;Z

def puzzle1(stra):
    points = 0
    for e in stra:
        if e.endswith('X'):
            points += 1
        elif e.endswith('Y'):
            points += 2
        elif e.endswith('Z'):
            points +=3

        if (e.startswith('A') and e.endswith('Z')) or (e.startswith('B') and e.endswith('X')) or (e.startswith('C') and e.endswith('Y')):
            continue
        elif (e.startswith('A') and e.endswith('X')) or (e.startswith('B') and e.endswith('Y')) or (e.startswith('C') and e.endswith('Z')):
            points += 3
        elif (e.startswith('A') and e.endswith('Y')) or (e.startswith('B') and e.endswith('Z')) or (e.startswith('C') and e.endswith('X')):
            points += 6

    return points

def puzzle2(stra):

    # X for lose
    # Y for draw
    # Z for win

    points = 0
    for e in stra:
        if e.endswith('X'):
            if e.startswith('A'):
                points += 3
            elif e.startswith('B'):
                points += 1
            elif e.startswith('C'):
                points += 2
        elif e.endswith('Y'):
            points += 3
            if e.startswith('A'):
                points += 1
            elif e.startswith('B'):
                points += 2
            elif e.startswith('C'):
                points += 3
        elif e.endswith('Z'):
            points += 6
            if e.startswith('A'):
                points += 2
            elif e.startswith('B'):
                points += 3
            elif e.startswith('C'):
                points += 1
    
    return points


print(puzzle1(stra))
print(puzzle2(stra))