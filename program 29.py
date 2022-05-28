#2. Write a program to display those string which starts with ‘A’ from the given list.
L=['AUSHIM','LEENA','AKHTAR','HIBA','NISHANT','AMAR']
count=0
for i in L:
    if i[0] in ('aA'):
        count=count+1
        print(i)
print("appearing",count,"times")   
