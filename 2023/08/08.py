instructions = []
nodes = dict()

with open('inputc..txt', 'r') as file:
    for line in file:
        if not '=' in line and not '' == line.strip():
            instructions = [x for x in line.strip()]
        elif '=' in line:
            nodes.update({line.split(' = ')[0].strip(): (line.split(' (')[1].split(', ')[0], line.split(', ')[1].split(')')[0])})


def part1():
    current_node = nodes.get('AAA')
    steps = 0
    end = False
    while not end:
        for d in instructions:
            steps += 1
            if d == 'R':
                current_node = nodes.get(current_node[1])
            else:
                current_node = nodes.get(current_node[0])

            if 'ZZZ' in  [k for k, v in nodes.items() if v == current_node]:
                end = True

    print(f'part1: {steps}')


part1()