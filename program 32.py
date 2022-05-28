#5. A list num contains the following elements : 3,21,5,6,14,8,14,3 .
 #Write a program to  swap the content with next value, if it is divisible by 7 so that  the  resultant array will  look like : 3,5,21,6,8,14,3,14
num=[3,21,5,6,14,8,14,3]
l=len(num)
i=0
print("the elements of the list is ",num)
while i<10:
    if num[i]%7==0:
        num[1],num[i+1]=num[i+1],num[i]
        i=i+2
    else:
        i=i+1
print("the elements of the list after swapping is ", num)   
