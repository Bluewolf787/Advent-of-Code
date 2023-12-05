from string import ascii_letters, digits

def get_data():
    data = []

    with open('./input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    # print(data)
    return data

def puzzle1(data):
    sum = 0
    i = 0
    while i < len(data):
        digit = ''
        valid = False
        isnum = False
        numend = False
        j = 0
        while j < len(data[i]):
            if data[i][j].isdigit():
                isnum = True
                if j+1 == len(data[i]) or not data[i][j+1].isdigit():
                    numend = True
             
                if j > 0:
                    if set(data[i][j-1]).difference(ascii_letters + digits) and not '.' in set(data[i][j-1]).difference(ascii_letters + digits):
                        valid = True
                if j+1 < len(data[i]):
                    if set(data[i][j+1]).difference(ascii_letters + digits) and not '.' in set(data[i][j+1]).difference(ascii_letters + digits):
                        valid = True
                if i > 0:
                    if set(data[i-1][j]).difference(ascii_letters + digits) and not '.' in set(data[i-1][j]).difference(ascii_letters + digits):
                        valid = True
                    if j+1 < len(data[i]):
                        if set(data[i-1][j+1]).difference(ascii_letters + digits) and not '.' in set(data[i-1][j+1]).difference(ascii_letters + digits):
                            valid = True
                    if j > 0:
                        if set(data[i-1][j-1]).difference(ascii_letters + digits) and not '.' in set(data[i-1][j-1]).difference(ascii_letters + digits):
                            valid = True
                if i+1 < len(data):
                    if set(data[i+1][j]).difference(ascii_letters + digits) and not '.' in set(data[i+1][j]).difference(ascii_letters + digits):
                        valid = True
                    if j+1 < len(data[i]):
                        if set(data[i+1][j+1]).difference(ascii_letters + digits) and not '.' in set(data[i+1][j+1]).difference(ascii_letters + digits):
                            valid = True
                    if j > 0:
                        if set(data[i+1][j-1]).difference(ascii_letters + digits) and not '.' in set(data[i+1][j-1]).difference(ascii_letters + digits):
                            valid = True
                
                digit += data[i][j]

            if numend and isnum:
                if valid:
                    sum += int(digit)
                    valid = False
                numend = False
                isnum = False
                digit = ''

            if not data[i][j].isdigit():
                isnum = False
                valid = False
            j += 1
        i += 1

    print(sum)


def puzzle2(data):
    pass
             

puzzle1(get_data()) # 522726
puzzle2(get_data())