#4. Write a program that inputs a student’s marks in three subjects (out of 100) and prints the percentage marks.

print('Enter the marks of three subject out of 100')
a=float(input('Enter the marks of first subject:'))
b=float(input('Enter the marks of second subject:'))
c=float(input('Enter the marks of third subject:'))
P=(a+b+c)/3
print('The percentage marks are:', P,'%')
