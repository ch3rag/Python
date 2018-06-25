#Program to collect all the divisors of a number

def gatherDivisor (number):
	divisor = []
	for div in range(1, number+1):
		if number % div == 0:
			divisor.append(div)
	return divisor
  
#EXAMPLE

print(gatherDivisor(55))

#[1, 5, 11, 55]
