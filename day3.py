#Exercises - Day 3
#Point 1-3
age = int(30)
height = float(230)
cmplx_nr = complex(1+1j)

#Point 4
trig_base = float(input("Triangle base: "))
trig_height = float(input("Triangle height: "))
trig_area = 0.5 * trig_base * trig_height
print("Triangle area is: ", trig_area)

#Point 5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
trig_perimeter = side_a + side_b + side_c
print("Triangle perimeter is: ", trig_perimeter)

#Point 6
rect_len = float(input("Rectangle lenght: "))
rect_width = float(input("Rectangle width: "))
rect_area = rect_len * rect_width
rect_perimeter = 2 * rect_len + rect_width
print("Rectangle area is:", rect_area , "and perimeter is:", rect_perimeter)

#Point 7
import math
radius = float(input("Circle readius: "))
circle_area = radius ** 2 * math.pi
circle_circumf = radius * 2 * math.pi
print("Circle area is:", round(circle_area,3) , "and circumference is:", round(circle_circumf,2))
