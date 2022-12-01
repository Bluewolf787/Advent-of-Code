calories = 0
calories_list = []

with open('/home/richard/Development/Advent-of-Code/2022/01/input.txt', 'r') as file:
    for line in file:
        if line.strip() == '':
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line.strip())

calories_list.sort

print(calories_list[-1:])
print(sum(calories_list[-3:]))