import base64
# Creating a string
s = "Hello World! I am Phika..."

# Encoding the string into bytes
b = s.encode("UTF-8")
print(2, b)

# Base64 Encode the bytes
e = base64.b64encode(b)
print(3, e)

# Decoding the Base64 bytes to string
s1 = e.decode("UTF-8")

# Printing Base64 encoded string
print("Base64 Encoded:", s1, type(s1))

# Encoding the Base64 encoded string into bytes
b1 = s1.encode("UTF-8")
print(5, b1, type(b1))

# Decoding the Base64 bytes
d = base64.b64decode(b1)
print(6, d, type(d))

# Decoding the bytes to string
s2 = d.decode("UTF-8")
print(s2, type(s2))


# ------------
# encode(str):  >>> byte
# decode(byte):  >>> str
# base64.encode(byte):  >>> byte
# base64.decode(byte):  >>> byte
