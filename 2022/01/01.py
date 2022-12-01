# Advent of Code Day 01
# Puzzle 01

def get_elf_calories_count():
    calories = 0
    calories_list = []

    with open('/home/richard/Development/Advent-of-Code/2022/01/input.txt', 'r') as file:
        for line in file:
            if line.strip() == '':
                calories_list.append(calories)
                calories = 0
            else:
                calories += int(line.strip())

    return calories_list

def puzzle1(list):
    index = 0
    max_cal = 0
    for cal in list:
        if cal >= max_cal:
            max_cal = cal
            index = list.index(cal)
        else:
            index = list.index(max_cal)

    print('The %d. elf has the most calorines with %d in total' % (index + 1, max_cal))
    return max_cal

def get_max_calories(list, limit):
    calories = 0;
    for cal in list:
        if cal < limit and cal >= calories:
            calories = cal
    
    return calories

def puzzle2(list):
    max_cal = puzzle1(list)
    sec_max_cal = get_max_calories(list, max_cal)
    third_max_cal = get_max_calories(list, sec_max_cal)
    
    total = max_cal + sec_max_cal + third_max_cal

    print('The top three elfs have 1. %d, 2. %d, 3. %d calorines and a total of %d calorines' % (max_cal, sec_max_cal, third_max_cal, total))

calories_list = get_elf_calories_count()
#puzzle1(calorines_list)
puzzle2(calories_list)