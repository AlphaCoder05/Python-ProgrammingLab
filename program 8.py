#8.Write a program that accepts weight in Kg and height in meters and calculate the BMI.
W = float(input('Enter the weight in Kg:'))
H = float(input('Enter height in meters:'))
BMI=W/(H**2)
print('BMI is:', BMI)
