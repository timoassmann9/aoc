import hashlib

key_start = "iwrupvqb"

for i in range(1000000):
    key = key_start + str(i)
    res = hashlib.md5(key.encode())
    hex = res.hexdigest()

    leading_zeros = 0
    if hex[0] == "0":
        leading_zeros += 1

    for idx in range(1, len(hex)):
        if hex[idx] == "0" and hex[idx-1] == "0":
            leading_zeros += 1
        else:
            break

    if leading_zeros > 4:
        print(key)
        print(hex)
        break