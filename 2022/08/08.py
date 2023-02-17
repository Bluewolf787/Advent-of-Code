
def get_input():
    grid = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = []
            for c in line.strip():
                row.append(int(c))
            grid.append(row.copy())

    # print(grid)
    return grid

def puzzle1(grid):
    visible = len(grid[0]) * 2
    for i in range(1, len(grid) - 1):
        visible += 2

        for j in range(1, len(grid[i]) - 1):
            

        break

    return visible


grid = get_input()
print(puzzle1(grid.copy()))
