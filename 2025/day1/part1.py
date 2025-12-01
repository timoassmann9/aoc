with open("input.txt", "r") as f:
    input = f.read()

rotations_list = input.split()

dial = 50
password = 0

for rotation in rotations_list:
    direction = rotation[0]
    distance = int(rotation[1:])
    if distance > 99:
        distance %= 100

    if direction == "R":
        dial += distance
        if dial > 99:
            dial %= 100

    if direction == "L":
        dial -= distance
        if dial < 0:
            dial += 100
    
    if dial == 0:
        password += 1

print(password)