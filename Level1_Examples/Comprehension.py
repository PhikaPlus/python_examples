# [ expression for item in list if conditional ]
a = (x ** 2 for x in range(10))
print(list(a))

# ------------------------------------------------------
# b = [x*2 for x in range(10) if x % 2 == 0]
b = [x*2
	 for x in range(10)
	 if x % 2 == 0]
print(b)

# ------------------------------------------------------
c = [(x, y, z)
	for x in range(1, 20)
	for y in range(x, 20)
	for z in range(y, 20)
	if x**2 + y**2 == z**2]
print(c)

# ------------------------------------------------------
d = [x*2 + y*2
	 for x in range(10)
	 for y in range(10)
	 if x % 2 == 0 and y > 5]
print(d)


