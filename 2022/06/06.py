data = ''
buffer = []
with open('input.txt', 'r') as file:
    for line in file:
        data = line.strip()
        for i in range(0, len(line.strip()) - 3):
            buffer.append(line.strip()[i:i+4])


def puzzle1(data):
    pos = -1
    for seq in data:
        if seq[0] == seq[1] or seq[0] == seq[2] or seq[0] == seq[3]:
            continue
        elif seq[1] == seq[2] or seq[1] == seq[3]:
            continue
        elif seq[2] == seq[3]:
            continue
        else:
            pos = data.index(seq) + 4
            break

    return pos


def puzzle2():
    unique_chars = 14
    for index in range(0, len(data)-(unique_chars-1)):
        if (len((set(data[index:index+unique_chars]))) == unique_chars):
            return index+unique_chars

print(puzzle1(buffer))
print(puzzle2())