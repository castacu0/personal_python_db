def fibonnacci(num):
    if num == 0 or num == 1: #if these are TRUE 
      return 1 #base cases
    return fibonnacci(num - 1) + fibonnacci(num - 2) 
#rememeber it has parameters. 👆
    # if they are FALSE
fibonnacci(5)
print("The following number after 5 in the sequence is", fibonnacci(5))