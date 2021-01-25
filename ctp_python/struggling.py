def trying(n):
  if(n > 0):
    print(".")
    result = n + trying(n - 1)
    print(f"Now I changed {trying(n-1)}")
    print(result)
    return result
  else:
    result = 0
    print("else")
    return result
  #return result

print("\n\nRecursion Example Results")
trying(6)