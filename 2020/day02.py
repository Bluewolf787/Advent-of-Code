## -- DAY TWO OF ADVENT OF CODE -- ##
#
# Day 02 - https://adventofcode.com/2020/day/2
#

passwords = []

with open('D:\\Learning\\Advent_of_Code\\puzzle_input\\day02_input.txt') as f:
    passwords = list(map(str, f.readlines()))

# -- Part One -- #
def part_one(l):
    valid = 0
    password = ''
    policy = ''

    occurrence = 0

    lowest = 0
    highest = 0
    given_letter = ''

    for item in l:
        policy = item[:item.find(': ')]
        #print(policy) 
        password = (item[item.find(': '):][2:-1])
        #print(password)
        lowest = int(policy[:policy.find('-')])
        #print(lowest)
        highest = int((policy[policy.find('-'):][1:-2]))
        #print(highest)
        given_letter = (policy[policy.find(' '):][1:])
        #print(given_letter)
        occurrence = password.count(given_letter)
        #print(occurrence)
        if occurrence >= lowest and occurrence <= highest:
            valid += 1

    print('Answer for Part One: ' + str(valid))

part_one(passwords)


# -- Part Two -- #
def part_two(l):
    valid = 0
    password = ''
    policy = ''

    occurrence = 0

    first_pos = 0
    sec_pos = 0
    first_letter = ''
    sec_letter = ''
    given_letter = ''

    for item in l:
        policy = item[:item.find(': ')]
        #print(policy) 
        password = (item[item.find(': '):][2:-1])
        #print(password)
        first_pos = int(policy[:policy.find('-')])
        #print(lowest)
        sec_pos = int((policy[policy.find('-'):][1:-2]))
        #print(highest)
        given_letter = (policy[policy.find(' '):][1:])
        #print(given_letter)

        first_letter = str(password[first_pos - 1])
        sec_letter = str(password[sec_pos - 1])
        if (first_letter == given_letter and sec_letter != given_letter) or (first_letter != given_letter and sec_letter == given_letter):
            valid += 1

    print('Answer for Part Two: ' + str(valid))

part_two(passwords)