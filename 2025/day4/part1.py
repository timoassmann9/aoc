def is_paper(obj: str):
    return obj == "@"

def check(grid, pos):
    row, column = pos
    try:
        return grid[row][column]
    except IndexError:
        return ""

def is_accessible(grid: list[str], pos: tuple[int, int]):
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
accessible_rolls = 0

for i in range(2):
    print(f"row: {i}")
    for j in range(len(grid[i])):
        if not is_paper(grid[i][j]):
            continue
        if is_accessible(grid, (i, j)):
            accessible_rolls += 1
            print(f"Rolle an Position {j} ist accessible")
        else:
            print(f"Rolle an Position {j} ist nicht accessible")

print(accessible_rolls)