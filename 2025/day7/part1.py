with open("input.txt") as f:
    data = f.read()
    
total_splits = 0

data = data.split()
data = [list(x) for x in data]

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            data[i+1][j] = "|"
            break
        if data[i-1][j] == "|":
            if char == "^":
                total_splits += 1
                data[i][j-1] = "|"
                data[i][j+1] = "|"
            if char == ".":
                data[i][j] = "|"

print(total_splits)