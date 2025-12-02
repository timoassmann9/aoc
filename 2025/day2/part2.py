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

        if len(id) > 1:
            all_same_digits = True
            for digit in id:
                if digit != id[0]:
                    all_same_digits = False
                    break
            if all_same_digits:
                invalid_ids.append(int(id))
                continue

        possible_sequence_lengths = list()
        for i in range(2, len(id)):
            if len(id) % i != 0:
                continue
            possible_sequence_lengths.append((i, len(id)//i))

        if not possible_sequence_lengths:
            continue
        
        for sequences_number, sequence_length in possible_sequence_lengths:
            sequences = list()
            start = 0

            for _ in range(sequences_number):
                sequence = id[start:start+sequence_length]
                sequences.append(sequence)
                start += sequence_length
            
            all_same_sequences = True
            for sequence in sequences:
                if sequence != sequences[0]:
                    all_same_sequences = False
            
            if all_same_sequences:
                invalid_ids.append(int(id))
                break

print(sum(invalid_ids))