def get_data():
    time = []
    distance = []
    data = []

    with open('input.txt', 'r') as file:
        for line in file:
            if 'Time' in line:
                time = [int(num) for num in line.split() if num.isdigit()]
            else:
                distance = [int(num) for num in line.split() if num.isdigit()]
            
        data.append(time)
        data.append(distance)

    return data


def find_ways_to_beat(time: int, distance: int):
    ways_count = 0
    btn_time = 0
    race_time = 0
    speed = -1
    while btn_time < time:
        race_time = time - btn_time
        speed += 1
        if speed * race_time > distance and btn_time + race_time <= time:
            # print(f'{btn_time}ms / {speed * race_time}mm/ms ({speed}) / {race_time}ms')
            ways_count += 1

        btn_time += 1
    
    return ways_count

def part1(data):
    sum = 1
    i = 0
    while i + 1 <= len(data[0]):
        time = data[0][i]
        distance = data[1][i]

        sum *= find_ways_to_beat(time, distance)
        
        i += 1
    
    print(f'Part 1: {sum}')

def part2(data):
    time = ''
    distance = ''
    i = 0
    while i + 1 <= len(data[0]):
        time += str(data[0][i])
        distance += str(data[1][i])
        i += 1

    sum = 0
    sum += find_ways_to_beat(int(time), int(distance))
    
    print(f'Part 2: {sum}')


part1(get_data()) # 275724
part2(get_data()) # 37286485