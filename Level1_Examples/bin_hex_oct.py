# Reaz Shah (instagram: Phika.ir)

# just enter an ***integer number***


def change_format(num):
	"""
	simply changes an integer number to bin, hex and oct format
	:param num:
	:return: bin, hex and oct format
	"""

	print('========== Bin ==========')
	print(bin(num))
	print(bin(-num))
	print(format(num, 'b'))
	print(format(num, '#b'))
	print(f'{num:b}')
	print(f'{num:#b}')
	print('========== Hex ==========')
	print(hex(num))
	print(hex(-num))
	print(format(num, 'x'))
	print(format(num, '#x'))
	print(f'{num:x}')
	print(f'{num:#x}')
	print('========== Oct ==========')
	print(oct(num))
	print(oct(-num))
	print(format(num, 'o'))
	print(format(num, '#o'))
	print(f'{num:o}')
	print(f'{num:#o}')

change_format(int(input('enter an integer number: \n')))
