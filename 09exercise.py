#circumference of a circle 
import math 
radius = float(input("Enter the radius of the circle in cm : "))
result = 2*math.pi*radius
print(f"The circumference of the circle is : {round(result,2)}")

#area of a circle  
radius2 = float(input("Enter the radius of the circle in cm :"))
area = math.pi*radius2**2
print(f"The area of the circle is {round(area,2)}cm²")
                                   

#hypotenuse of a Triangle
import math
perpendicular = float(input("Enter the perpendicular length of the triangle in cm :"))
base = float(input("Enter the base of the Triangle in cm : "))
hypotenuse = math.sqrt(perpendicular**2 + base**2)
print(round(hypotenuse,2))
