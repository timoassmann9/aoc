with open("input.txt", "r") as f:
    data = f.read()

banks = data.split()
max_joltages = list()
for bank in banks:
    possible_joltages = list()
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i] + bank[j])
            possible_joltages.append(joltage)
    max_joltage = max(possible_joltages)
    max_joltages.append(max_joltage)

print(sum(max_joltages))