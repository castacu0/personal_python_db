# Python program to display the Fibonacci sequence

def do_math(num):
   if num <= 1:
       return num
   else:
       return(do_math(num-1) + do_math(num-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(do_math(i))