with open("input.txt", "r") as f:
    data = f.read()

floor = 0
for idx, instruction in enumerate(data, start=1):
    if instruction not in ("(", ")"):
        continue
    if instruction == "(":
        floor += 1
    if instruction == ")":
        floor -= 1
    
    if floor == -1:
        print(idx)
        break