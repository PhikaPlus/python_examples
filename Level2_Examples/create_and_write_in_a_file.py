import datetime

# a: indicates "append"
# +: means it will create a file if it does not exist in library
# 'a+'

# open or create file
file = open("Log.txt", "a+")    # File name and mode
t = datetime.datetime.now()

# write in file
for i in range(1, 10):
	file.write('{}: line {}\n'.format(t, i))
file.write('\n')                # create a empty line after writing finishes

file.close()                    # close file at the end of proccess
