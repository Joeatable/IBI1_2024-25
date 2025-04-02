# What does this piece of code do?
# Answer:
# [to calculate how many rounds could two "dice" that 
# create two numbers randomly are the same. ]
# Or: create two numbers(first_n\second_n) between 1-6 randomly until they are the same (if first_n == second_n:)
# and then break the loop, calculating the number of attemps(progress)

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 
while progress>=0:
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break

