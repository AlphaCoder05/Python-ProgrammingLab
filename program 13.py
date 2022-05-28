#13.Write a program to find sum of series :
#s=1+x+x²+x³+x⁴…+xⁿ
x=float(input('Enter the value of x:'))
n=int(input('Enter the value of n (for x**n):'))
s=0
for a in range(n+1):
    s+=x**a
print('Sum of first' ,n,'terms:',s)
