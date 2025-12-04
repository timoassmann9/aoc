def get_max_joltage(bank: str, digits):
    result = ""
    start = 0

    for pos in range(digits):
        remaining = digits - pos
        end = len(bank) - remaining
        best_char = max(bank[start:end+1])
        best_index = bank.index(best_char, start, end+1)

        result += best_char
        start = best_index + 1

    return result

with open("input.txt", "r") as f:
    data = f.read()

banks = data.split()
max_joltages = list()
for bank in banks:
    max_joltage = get_max_joltage(bank, 12)
    max_joltages.append(int(max_joltage))

print(sum(max_joltages))