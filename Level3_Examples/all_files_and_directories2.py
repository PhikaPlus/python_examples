import os

def list_dir(directory):
	a = os.listdir(directory)
	for i, item in enumerate(a):	 # All files
		if os.path.isdir(item):
			print(i, 'Directory:    ', item)
		else:
			print(i, 'File:         ', item)


list_dir(current_dir)
