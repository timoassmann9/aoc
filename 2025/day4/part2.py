def is_paper(obj: str):
    return obj == "@"

def check(grid, pos):
    row, column = pos
    if (
        -1 < row < len(grid) and
        -1 < column < len(grid[row])
    ):
        return grid[row][column]
    return ""

def is_accessible(grid: list[list[str]], pos: tuple[int, int]):
    row, column = pos
    adjacent_rolls = 0

    n = row - 1, column
    ne = row -1, column + 1
    e = row, column + 1
    se = row + 1, column + 1
    s = row + 1, column
    sw = row + 1, column - 1
    w = row, column - 1
    nw = row - 1, column - 1

    adjacent_pos = [n, ne, e, se, s, sw, w, nw]

    for position in adjacent_pos:
        if is_paper(check(grid, position)):
            adjacent_rolls += 1

    if adjacent_rolls > 3:
        return False
    
    return True

with open("input.txt", "r") as f:
    data = f.read()

grid = data.split()
grid = [list(x) for x in grid]

total_accessible_rolls = 0
while True:
    accessible_rolls = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not is_paper(grid[i][j]):
                continue
            if is_accessible(grid, (i, j)):
                accessible_rolls += 1
                grid[i][j] = "."

    total_accessible_rolls += accessible_rolls
    if not accessible_rolls:
        break

print(total_accessible_rolls)