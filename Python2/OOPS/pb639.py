# Write a program to find the distance between two points in cartesian cordinate system

import math

x1=float(input("Enter a number x1:"))
y1=float(input("Enter a number y1:"))

x2=float(input('Enter a number x2:'))
y2=float(input("Enter a number y2:"))

distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance between two point is:",distance)

