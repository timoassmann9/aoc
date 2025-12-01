with open("input.txt", "r") as f:
    input = f.read()

floor = 0
for instruction in input:
    if instruction not in ("(", ")"):