'''Python program to convert number into sring
that contains raindrop sound'''

def convert(number):
    result = " "
    
# if has 3 as a factor, "pling" to result    
    if number % 3 == 0:
       result += "Pling"
    
# if has 5 as a factor, "plang" to result    
    if number % 5 == 0:
       result += "Plang"

# if has 7 as a factor, "plong" to result    
    if number % 7 == 0:
       result += "Plong"
    
# if doesn't have factor, 	   
    if result is " ":
		return str(number)

return result
