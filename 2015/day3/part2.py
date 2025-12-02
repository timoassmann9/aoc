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

def add_house(houses: list, pos: tuple):
    houses.append(pos)

pos_santa = 0, 0
pos_robo = 0, 0
houses = []
add_house(houses, pos_santa)

for i, direction in enumerate(data, start=1):
    if i % 2 != 0:
        pos_santa = move(pos_santa, direction)
        if pos_santa not in houses:
            add_house(houses, pos_santa)

    if i % 2 == 0:
        pos_robo = move(pos_robo, direction)
        if pos_robo not in houses:
            add_house(houses, pos_robo)
    
print(len(houses))