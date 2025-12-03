import hashlib

key_start = "iwrupvqb"

for i in range(1000000):
    key = key_start + str(i)
    res = hashlib.md5(key.encode())
    hex = res.hexdigest()

    leading_zeros = 0
    for idx, char in enumerate(hex):
        if idx == 0 and char == "0":
            leading_zeros += 1