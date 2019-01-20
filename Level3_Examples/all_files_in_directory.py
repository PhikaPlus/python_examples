# only returns files names in a directory

import os
import glob


def list_files(directory):
	os.chdir(directory)
	for i, file in enumerate(glob.glob('*.*')):	 # All files
		print(i, ':    ', file)


# specific_dir = "E:\\Phika.ir\\Py"		# Specific Directory
current_dir = os.getcwd()				# Current Directory
list_files(current_dir)
