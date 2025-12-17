def one(string):
    for i in range(len(string)-3):
        one = string[i:i+2]
        for j in range(i+2, len(string)-1):
            two = string[j:j+2]
            if one == two:
                return True
    return False
            

def two(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False
        

with open("input.txt") as f:
    data = f.read()

strings = data.split()

nice = 0
for string in strings:
    if one(string) and two(string):
        nice += 1

print(nice)