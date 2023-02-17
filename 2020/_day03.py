## -- DAY THREE OF ADVENT OF CODE -- ##

tree_map = []

with open('D:\\Learning\\Advent_of_Code\\puzzle_input\\trees_input.txt') as f:
    tree_map = list(map(str, f.readlines()));

# -- Part One -- #
def part_one(l):
    position = 0
    tree = '#'
    trees_hit = 0

    for row in l:
       for coords in row:
           if coords[position] == tree:
                trees_hit += 1

            position += 3

    print(trees_hit)

part_one(tree_map)

# -- Part Two -- #
def part_two(l):
    None