## -- DAY THREE OF ADVENT OF CODE -- ##
#
# Day 03 - https://adventofcode.com/2020/day/3
#

with open('D:\\Learning\\Advent_of_Code\\puzzle_input\\day03_input.txt') as f:
    data = f.read()

rows = [ x for x in data.split('\n') if x ]

def arboreal_stop(right, down):
    position = 0
    trees_hit = 0

    for chunk in range(0, len(rows), down):
        trees_hit += int(rows[chunk][position] == '#')
        position = (position + right) % len(rows[chunk])

    return trees_hit


# -- Part One -- #
print(f'Answer for Part One: {arboreal_stop(3, 1)}')

# -- Part Two -- #
print(f'Answer for Part Two: {arboreal_stop(1, 1) * arboreal_stop(3, 1) * arboreal_stop(5, 1) * arboreal_stop(7, 1) * arboreal_stop(1, 2)}')
