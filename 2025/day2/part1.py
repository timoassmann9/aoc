with open("input.txt", "r") as f:
    data = f.read()

id_ranges = data.split(",")
invalid_ids = list()
for id_range in id_ranges:
    if not "-" in id_range:
        continue

    start_end_list = id_range.split("-")
    if len(start_end_list) != 2:
        continue
    
    start_id = int(start_end_list[0])
    end_id = int(start_end_list[1])

    for id in range(start_id, end_id+1):
        id = str(id)
        if len(id) % 2 != 0:
            continue

        first_half = id[:len(id)//2]
        second_half = id[len(id)//2:]
        if first_half == second_half:
            invalid_ids.append(int(id))

print(sum(invalid_ids))