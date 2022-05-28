# STRIN PROGRAMS IN PYTHON
#1. Program that reads a line and print its statistics like:
#Number of uppercase letters:
#Number of lowercase letters:
#Number of alphabets:
#Number of digits


line=input('Enter a line:')
lowercount=uppercount=0
digitcount=alphacount=0

for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
if a.isalpha():
        alphacount+=1

print('Number of uppercase letters are:',uppercount)
print('Number of lowercase letters are:',lowercount)
print('Number of alphabets are:',alphacount)
print('Number of digits are:',digitcount)
