with open("input.txt", "r") as f:
    data = f.read()

def move(pos: tuple, direction: str):
    x, y = pos
    if len(direction) > 1:
        print("Only one move at a time!")

    if direction == "^":
        x += 1
    if direction == "v":
        x -= 1
    if direction == ">":
        y += 1
    if direction == "<":
        y -= 1
    
    return x, y

def visit_house(track: list, pos: tuple):
    track.append(pos)

x = 0
y = 0
pos = x, y
visited = []
visit_house(visited, pos)

for direction in data:
    pos = move(pos, direction)
    if pos not in visited:
        visit_house(visited, pos)
    
print(len(visited))