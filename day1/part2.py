with open("input.txt", "r") as f:
    input = f.read()

rotations_list = input.split()

dial = 50
password = 0

for rotation in rotations_list:
    direction = rotation[0]
    distance = int(rotation[1:])
    full_rotations = 0
    if distance > 99:
        full_rotations = distance // 100
        distance %= 100

    if direction == "R":
        dial += distance
        if dial > 99:
            dial %= 100
            password += 1

    if direction == "L":
        do_not_count = True if dial == 0 else False
        dial -= distance
        if dial < 1:
            password += 0 if do_not_count else 1
            if dial < 0:
                dial += 100

    password += full_rotations

print(password)