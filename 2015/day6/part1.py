def exec(start, end, instruction):
    global grid

    start_x, start_y = start
    end_x, end_y = end

    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            match instruction:
                case "turn on":
                    grid[i][j] = 1
                case "turn off":
                    grid[i][j] = 0
                case "toggle":
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

with open("input.txt") as f:
    data = f.read()

data = data.split("\n")

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in data:
    for i, char in enumerate(instruction):
        if char.isnumeric():
            break
    through_start = instruction.index("through")
    through_end = through_start + 7
    c1 = tuple(map(int, instruction[i:through_start-1].split(",")))
    c2 = tuple(map(int, instruction[through_end+1:len(instruction)].split(",")))
    instruction = instruction[:i-1]
    exec(c1, c2, instruction)

print(sum(line.count(1) for line in grid))