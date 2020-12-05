"""
This program takes the radius value that is entered by the user and figures out and displays the area and circumference of the circle
"""
import math 
radius = int(input("What is the radius?: ")) #ask for the radius of the circle, conver to int
print(f"The area is: {round(math.pi*(radius**2),1)}") #area of the circle is printed
print (f"The circumference is:100 {round(2*math.pi*radius,1)}")#circumference of the circle is printed