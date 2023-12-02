def get_data():
    data = []

    with open('./input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    return data

def puzzle1(data):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    sum = 0
    for line in data:
        nums = []
        for digit in line:
            if digit in digits:
                nums.append(digit)
        # sum += int(nums[0]) * 10 + int(nums[-1])

    print(sum)

def puzzle2(data):
    digits = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),(5, 'five') ,(6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'),
       (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'),(8, '8'), (9, '9')]
    sum = 0
    
    for line in data:
        x = 0
        y = 0
        occ = []

        for a, b in digits:
            if b in line:
                occ.append((a, line.find(b)))
        
        # print(occ)
        min = 99999
        max = 0
        for a, b in occ:
            if 0 <= b < min:
                x = a
                min = b
            if max < b:
                y = a
                max = b
        
        if y == 0:
            y = x
        
        # print('x: %d -- y: %d' % (x, y))
        sum += (x * 10) + y

    print(sum)

puzzle1(get_data()) # 53974
puzzle2(get_data()) # 52840

