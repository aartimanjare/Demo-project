def Square_Difference(n):

	# first n natural numbers 
	A = (n * (n + 1) * (2 * n + 1)) / 6
	
	# sum of n naturals numbers
	B = (n * (n + 1)) / 2
	# square of n naturals number
	B = B ** 2
	
	# Differences between A and B
	C = abs(A - B)
	
	return C

# Driver code
print(Square_Difference(15))
