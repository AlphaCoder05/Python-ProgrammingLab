#4. Write a program to show sorting of elements of a list step-by-step.
a=[16,10,2,4,9,18]
print("the unsorted list is ",a)
print("the sorting starts now:")
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]
    print("the list after sorting " , i ,"loop is",a)        
print("the list after sorting is",a)        
