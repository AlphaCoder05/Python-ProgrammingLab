#7.Write a program to find factorial of a number in Python using Function.
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)
print(factorial(5))