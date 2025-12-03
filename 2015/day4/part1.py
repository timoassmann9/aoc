import hashlib

res = hashlib.md5(b"abc")
hex = res.hexdigest()
print(hex.startswith("9000"))
