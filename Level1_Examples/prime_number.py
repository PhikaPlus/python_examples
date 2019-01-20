def is_this_prime(input_number):
	for i in range(2, (int(input_number/2) + 1)):
	    if input_number % i == 0:
	        return False
	    else:
	        return True


a = is_this_prime(7)
print(a)
