from collections import Counter

def get_data():
    hands = []
    bids = []
    data = []

    with open('input.txt', 'r') as file:
        for line in file:
            hands.append(line.split(' ')[0].strip())
            bids.append(line.split(' ')[1].strip())
        data.append(hands)
        data.append(bids)

    return data

def get_hand_type(hands):
    five = []
    four = []
    full_house = []
    three = []
    two_pair = []
    one_pair = []
    high = []
    for hand in hands:
        char_counter = Counter(hand)
        if 5 in char_counter.values():
            five.append(hand)
        elif 4 in char_counter.values():
            four.append(hand)
        elif 3 in char_counter.values() and 2 in char_counter.values():
            full_house.append(hand)
        elif 3 in char_counter.values():
            three.append(hand)
        elif len([count for count in char_counter.values() if count == 2]) == 2:
            two_pair.append(hand)
        elif 2 in char_counter.values():
            one_pair.append(hand)
        else:
            high.append(hand)
    
    return [five, four, full_house, three, two_pair, one_pair, high] # {'five': five, 'four': four, 'full': full_house, 'three': three, 'two': two_pair, 'one': one_pair, 'high': high}

def swap(list, a: int, b: int):
    swaped_list = list
    x = swaped_list[a]
    swaped_list[a] = swaped_list[b]
    swaped_list[b] = x
    return swaped_list


cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def sort_func(s):
    prio = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return [prio[char] for char in s]

def sort_hands(type):
    return sorted(type, key=sort_func, reverse=True)


def part1(data):
    hand_types = get_hand_type(data[0])

    sorted_hands = []
    for hands in hand_types:
        sorted_hands.append(sort_hands(hands))

    # print(sorted_hands)
    total = 0
    rank = len(data[0])
    for type in sorted_hands:
        for hand in type:
            for h in data[0]:
                if h == hand:
                    #print(f'{h} {data[1][data[0].index(h)]}')
                    total += int(data[1][data[0].index(h)]) * rank
                    rank -= 1

    print(f'sum: {total}')


part1(get_data())