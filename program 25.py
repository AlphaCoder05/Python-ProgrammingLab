#3. Write a program that reads a string and checks whether it is a palindrome string or not.
string=input('Enter a string:')
length=len(string)
mid=length//2
rev=-1
for a in range(mid):
    if string[a]==string[rev]:
        print(string,'is a palindrome.')
    break
else:
    print(string,'is not a palindrome.')
