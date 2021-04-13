variable = "hello"   
#assert means:   checa si ___ es exactamente igual a ___ 

#if condition returns True, then nothing happens:
#assert variable == "hello"

#if condition returns False, AssertionError is raised:
#assert variable == "goodbye"


assert variable == "goodbye", "it should have been hello"