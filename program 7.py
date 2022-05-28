#7.Write a program to find lowest among three integer.
a=int(input('Enter the first integer:'))
b=int(input('Enter the second integer:'))
c=int(input('Enter the third integer:'))
if a<b and a<c:
    print(a, 'is the smallest integer')
if b<a and b<c:
    print(b, 'is the smallest integer')
if c<a and c<b:
    print(c, 'is the smallest integer')
