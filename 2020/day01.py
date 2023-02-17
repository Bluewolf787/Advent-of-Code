## -- DAY ONE OF ADVENT OF CODE -- ##
#
# Day 01 - https://adventofcode.com/2020/day/1
#

expense_report = []

with open('D:\\Learning\\Advent_of_Code\\puzzle_input\\day01_input.txt') as f:
    expense_report = list(map(int, f.readlines()))

# -- Part One -- #
def correct_entries(l):
    for num1 in l:
        for num2 in l:
            if num1 + num2 == 2020:
                print('Answer for Part One: ' + str(num1 * num2))

correct_entries(expense_report)


# -- Part Two -- #
def correct_three_entries(l):
    for num1 in l:
        for num2 in l:
            for num3 in l:
                if num1 + num2 + num3 == 2020:
                    print('Answer for Part Two: ' + str(num1 * num2 * num3))

correct_three_entries(expense_report)