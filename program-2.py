#"Difference between square of sum and sum of squares"

def Square_Difference(n):

	# first n natural numbers 
	A = (n * (n + 1) * (2 * n + 1)) / 6
	
	# sum of n natural numbers
	B = (n * (n + 1)) / 2
	# square of n natural numbers
	B = B ** 2
	
	# Differences between A and B
	C = abs(A - B)
	
	return C

# User code
print(Square_Difference(15))
