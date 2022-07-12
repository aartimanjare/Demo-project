# Calculates sum of multiples of
# A number upto B
def sum_of_multiples(A, B):

	# Number of multiples
	M = B / A

	# sum of first M natural numbers
	sum = M * (M + 1) / 2

	# sum of multiples
	result = A * sum

	print("Sum of multiples of ", A, " up to ", B, " = ", result)

# User Code
sum_of_multiples(1, 18)
