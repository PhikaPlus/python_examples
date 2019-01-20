import collections

1

text = '''Phika - Python is an interpreted
		  high-level programming language
		  for general-purpose programming'''

result = collections.Counter(text)

print(result)

# 2

word = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = collections.Counter(word)
print(result)


