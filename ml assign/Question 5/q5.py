#the radius of the circle is 30 meters
r=30


#to find the area of the circle
import math as M 
_area_of_circle = M.pi* r * r  
print (" The area of the given circle is: ", _area_of_circle)  



#to find circumference of the circle
_circum_of_circle= 2 * M.pi * r
print("the circumference of the circle is",_circum_of_circle)





#taking radius as user input
radius=int(input("enter the radius:"))
_area_of_circle=M.pi * radius * radius
print(_area_of_circle)