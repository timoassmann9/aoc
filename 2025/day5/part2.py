with open("input.txt", "r") as f:
    data = f.read()

data = data.split()

data = [id_range for id_range in data if "-" in id_range]

fresh_ingredient_id_ranges: list[range] = list()

for id_range in data:
    start, stop = map(int, id_range.split("-"))
    stop += 1
    fresh_ingredient_id_ranges.append(range(start, stop))

fresh_ingredient_id_ranges = sorted(fresh_ingredient_id_ranges, key=lambda x: x.start)

merged = list()
current = fresh_ingredient_id_ranges[0]

for id_range in fresh_ingredient_id_ranges[1:]:
    if id_range.start <= current.stop:
        current = range(current.start, max(current.stop, id_range.stop))
    if id_range.start > current.stop:
        merged.append(current)
        current = id_range

merged.append(current)

total_ids = sum(id_range.stop - id_range.start for id_range in merged)
print(total_ids)