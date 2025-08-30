

#hypotenuse of a Triangle
import math
perpendicular = float(input("Enter the perpendicular length of the triangle in cm :"))
base = float(input("Enter the base of the Triangle in cm : "))
hypotenuse = math.sqrt(perpendicular**2 + base**2)
print(round(hypotenuse,2))
