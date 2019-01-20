class Color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


print(Color.RED + 'Hello World !' + Color.END)
print(Color.GREEN + 'Hello World !' + Color.END)
print(Color.YELLOW + 'Hello World !' + Color.END)
print(Color.BLUE + 'Hello World !' + Color.END)
print(Color.BOLD + 'Hello World !' + Color.END)
