_stacks = {
    1: ['Z', 'V', 'T', 'B', 'J', 'G', 'R'],
    2: ['L', 'V', 'R', 'J'],
    3: ['F', 'Q', 'S'],
    4: ['G', 'Q', 'V', 'F', 'L', 'N', 'H', 'Z'],
    5: ['W', 'M', 'S', 'C', 'J', 'T', 'Q', 'R'],
    6: ['F', 'H', 'C', 'T', 'W', 'S'],
    7: ['J', 'N', 'F', 'V', 'C', 'Z', 'D'],
    8: ['Q', 'F', 'R', 'W', 'D', 'Z', 'G', 'L'],
    9: ['P', 'V', 'W', 'B', 'J']
}

_moves = []
with open('input.txt', 'r') as file:
    move = []
    for line in file:
        if line.startswith('move'):
            l = line.strip().split(' ')
            move.append(int(l[1]))
            move.append(int(l[3]))
            move.append(int(l[5]))
            _moves.append(move.copy())
            move.clear()

def cratemover9000(moves, stacks):
    for move in moves:
        stack_from = stacks.get(move[1]).copy()
        for i in range(move[0]):
            stacks.get(move[2]).insert(i, stack_from[(move[0] - 1) - i])
            stacks.get(move[1]).pop(0)

    return get_order(stacks)

def cratemover9001(moves, stacks):
    moving_crates = []
    for move in moves:
        stack_from = stacks.get(move[1]).copy()
        for i in range(move[0]):
            moving_crates.append(stack_from[i])
            stacks.get(move[1]).pop(0)
        
        for i in range(move[0]):
            stacks.get(move[2]).insert(i, moving_crates[i]);
        moving_crates.clear()


    return get_order(stacks)

def get_order(stacks):
    crates = ''
    for i in range(1, 10):
        crates += stacks.get(i)[0]

    return crates

# print(cratemover9000(_moves, _stacks))
print(cratemover9001(_moves, _stacks))
