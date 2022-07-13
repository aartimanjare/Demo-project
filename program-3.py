# determine what th nth prime number

number = int(input("Enter Nth Number:"))
x = 0
num = 2
l = 0

while (x != number):
   count = 0
   for i in range(2,num):
      if (num % i == 0):
         count+=1
         break
   if (count == 0):
      x+=1
      l = num
   num = num + 1
print (number,"th prime number is ",l)   

if number < 1:
        # when the prime function receives malformed input
        raise ValueError('there is no zeroth prime')
