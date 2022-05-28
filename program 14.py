#14.Write a python script to input two numbers and print their lcm and hcf.
x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if x%i==0 and y%i==0:
        hcf=i
lcm=(x*y)/hcf
print('The HCF of',x,'and',y,'is:',hcf)
print('The LCM of',x,'and',y,'is:',lcm)
