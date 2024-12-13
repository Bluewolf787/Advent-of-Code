def get_data():
    data = []
    list1 = []
    list2 = []

    with open('./input.txt', 'r') as file:
        for line in file:
            list1.append(int(line.split(' ')[0].strip()))
            list2.append(int(line.split(' ')[-1].strip()))

    data.append(list1)
    data.append(list2)

    return data

def calc_distance(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def part1(data):
    sum = 0

    list1 = sorted(data[0])
    list2 = sorted(data[1])

    length = len(list1) if len(list1) > len(list2) else len(list2)

    for i in range(length):
        if i >= len(list2):
            sum += calc_distance(list1[i], list2[int(len(list2) - 1)])
        else:
            sum += calc_distance(list1[i], list2[i])
    
    return sum

def part2(data):
    sum = 0

    for i in data[0]:
        counter = 0
        for j in data[1]:
            if i == j:
                counter += 1

        sum += i * counter

    print(sum)


print(part1(get_data()))
print(part2(get_data()))

