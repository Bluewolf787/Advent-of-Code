def get_data():
    data = []
    with open('input2.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    # print(data)
    return data


def expand_rows(data: list, multiplier: int):
    new_data = []
    for line in data:
        if '#' not in line:
            i = 0
            while i < multiplier:
                new_data.append(line)
                i += 1
        else:
            new_data.append(line)
    
    return new_data


def expand_cols(data: list, multiplier: int):
    new_data = []

    for _ in data:
        new_data.append('')

    i = 0
    while i + 1 <= len(data[0]):
        valid = True
        j = 0
        while j + 1 <= len(data):
            if data[j][i] == '#':
                valid = False
            j += 1
            
        if valid:
            k = 0
            while k + 1 <= len(data):
                new_data[k] += data[k][i] * multiplier
                k += 1
        else:
            k = 0
            while k + 1 <= len(data):
                new_data[k] += data[k][i]
                k += 1
        i += 1
            
    return new_data


def expand(data: list, multiplier: int):
    new_data = expand_cols(data, multiplier)
    return expand_rows(new_data, multiplier)


def find_sortest_path(pos: tuple, data: list):
    steps = 0
    i = pos[0]
    while i + 1 <= len(data):
        j = 0
        while j + 1 <= len(data[i]) and not (i == pos[0] and j == pos[1]):
            if data[i][j] == '#':
                steps += abs(i - pos[0]) + abs(j - pos[1])
            j += 1
        i += 1
    # print(f'STEPS: {steps}')
    
    return steps


def get_solution(data: list):
    total = 0
    i = 0
    while i + 1 <= len(data):
        j = 0
        while j + 1 <= len(data[i]):
            if data[i][j] == '#':
                total += find_sortest_path((i, j), data)
            j += 1
        i += 1
    
    return total


def part1(data: list):
    print(f'part1: {get_solution(expand(data, 2))}')
    

part1(get_data())
