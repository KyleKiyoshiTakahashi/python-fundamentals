# As part of this assignment, please create a function randInt() where:
# 	randInt() returns a random integer between 0 to 100
# 	randInt(max=50) returns a random integer between 0 to 50
# 	randInt(min=50) returns a random integer between 50 to 100
# 	randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().

def randInt():
	import random
	print(int(random.random()*100))
	print(int(random.random()*50))
	print(random.randrange(50,100,1))
	print(random.randrange(50,500,1))

randInt()

