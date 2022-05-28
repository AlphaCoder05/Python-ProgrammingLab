# LIST PRORAMS IN PYTHON
#1. Write a program to display frequencies of all the element of a  list.

L=[3,21,5,6,3,8,21,6]
L1=[]
L2=[]
for i in L:
    if i not in L2:
        x=L.count(i)
        L1.append(x)
        L2.append(i)
print('element','\t\t\t',"frequency")
for i in range (len(L1)):
                print(L2[i],'\t\t\t',L1[i])
