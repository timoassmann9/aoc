def one(string):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in vowels:
            count += 1
    return count > 2

def two(string):
    for i, char in enumerate(string):
        if i == 0:
            continue
        if char == string[i-1]:
            return True
    return False

def three(string):
    bad = ["ab", "cd", "pq", "xy"]
    for x in bad:
        if x in string:
            return False
    return True

with open("input.txt") as f:
    data = f.read()

strings = data.split()

nice = 0
for string in strings:
    if one(string) and two(string) and three(string):
        nice += 1

print(nice)