#  list all files and directories

import os

def list_dir(directory):
	a = os.listdir(directory)
	for i, item in enumerate(a):	 # All files
		print(i, ':    ', item)


list_dir(current_dir)
