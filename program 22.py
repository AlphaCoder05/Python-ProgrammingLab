#8. Write a program to find Fabonacci Series of a number in Python using Function
def fib(n): 
    if n<=1: 
 	    return 1 
    else: 
	    return fib(n-1)+fib(n-2) 
n = int(input("enter number"))  
for i in range(n): 
    print(fib(i)) 