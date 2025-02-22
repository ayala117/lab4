import math

num_sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the side length: "))
area=(num_sides * side_length ** 2 )/(4*math.tan(math.pi/num_sides))
print(f"The area of the polygon is: {area:.0f}") 


#Enter the number of sides: 4
#Enter the side length: 25
#he area of the polygon is: 625