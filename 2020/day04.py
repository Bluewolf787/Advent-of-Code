## -- DAY FOUR OF ADVENT OF CODE -- ##
#
# Day 04 - https://adventofcode.com/2020/day/4 
#

with open('D:\\Learning\\Advent_of_Code\\puzzle_input\\day04_input.txt') as f:
    data = f.read()

passports = [ x for x in data.split('\n\n') if x ]

def part_one(l):
    fields = []
    for passport in l:
        for x in passport:
            if x == ' ' or x == '\n':
                fields = [ y for y in passport.split(x) if y]

        print(fields)


part_one(passports)