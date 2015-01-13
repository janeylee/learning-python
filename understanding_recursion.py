'''
Write a program using recursion to determine if a number is a power of 2 or not. (not in the MIT course)
'''

def is_power_of_two(n):

    n = float(n)
#This is necessary because Python will always round your numbers after mathematical operations.
    if n == 2:
        return True
#This is the base case. Otherwise known as the case for which the function is done and you don't need to recurse further.  
   
    b = n/2
    if b < 1:
        return False
    return is_power_of_two(b)


print is_power_of_two(9)
print is_power_of_two(2)
print is_power_of_two(10)
print is_power_of_two(65)
print is_power_of_two(64)


'''
Print out the nth number of the Fibonacci sequence.
'''
def fib(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

'''
Find the greatest common denominator of two numbers a and b. 
'''
def gcd(a,b):
	if a < b:
		a, b = b, a
	if a%b == 0:
		return b
	else:
		rem = a%b
		a = b
		b = rem
	return gcd(a,b)

print gcd(210, 45)
