import itertools

password = '12AB'
result = itertools.permutations(password)

for item in result:
	# print(item)					# returns a tuple
	print(''.join(list(item)), end = ' | ')		# all possible combinations

