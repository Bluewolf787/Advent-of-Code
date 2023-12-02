import re

def get_data():
    data = []

    with open('./input.txt', 'r') as file:
        for line in file:
            gameId = int(line.split(':')[0].split(' ')[1].strip())
            rounds = line.split(':')[1].strip()

            data.append((gameId, rounds.split(';')))

    # print(data)
    return data

def puzzle1(data):
    sum = 0

    for a, b in data:
        possible = True
        for round in b:
            red = 0
            green = 0
            blue = 0
            for i in round.split(','):
                i = i.split()
                if 'red' in i:
                    red += int(i[0])
                if 'green' in i:
                    green += int(i[0])
                if 'blue' in i:
                    blue += int(i[0])

                if red > 12 or green > 13 or blue > 14:
                    possible = False

        if possible:
            sum += a

    print(sum)

def puzzle2(data):
    sum = 0

    for a, b in data:
        power = 0
        red = 1
        green = 1
        blue = 1
        for round in b:
            for i in round.split(','):
                i = i.split()
                if 'red' in i and red < int(i[0]):
                    red = int(i[0])
                if 'green' in i and green < int(i[0]):
                    green = int(i[0])
                if 'blue' in i and blue < int(i[0]):
                    blue = int(i[0])

            power = red * green * blue
        
        sum += power

    print(sum)

puzzle1(get_data())
puzzle2(get_data())