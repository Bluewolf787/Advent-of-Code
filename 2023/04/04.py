def get_data():
    data = []

    with open('./input.txt', 'r') as file:
        for line in file:
            data.append(([int(num) for num in line.split(': ')[1].split('|')[0].strip().split()], [int(num) for num in line.split('|')[1].strip().split()]))

    # print(data)
    return data

def puzzle1(data):
    card = 0
    sum = 0
    for winning, have in data:
        for w in winning:
            for h in have:
                if w == h:
                    if card == 0:
                        card = 1
                    else: 
                        card *= 2
        sum += card
        card = 0
    print(sum)

def puzzle2(data):
    pass


puzzle1(get_data()) # 20107
puzzle2(get_data())