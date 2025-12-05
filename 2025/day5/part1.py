with open("input.txt", "r") as f:
    data = f.read()

data = data.split()

fresh_ingredient_id_ranges = [id_range for id_range in data if "-" in id_range]
available_ingredient_ids = [id for id in data if "-" not in id]

fresh_available_ingredients = 0
for id in available_ingredient_ids:
    id = int(id)
    for id_range in fresh_ingredient_id_ranges:
        first, last = map(int, id_range.split("-"))
        if id in range(first, last+1):
            fresh_available_ingredients += 1
            break

print(fresh_available_ingredients)