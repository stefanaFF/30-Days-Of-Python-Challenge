#Day 2

#Exercises: Level 1
#Points 1-12
first_name = "Stefana"
last_name = "FF"
full_name = first_name + " " + last_name
country = "Romania"
city = "Bucharest"
age = 30
year = 2023
is_married = False
is_true = True
is_light_on = False

#Points 13 - Declare multiple variable on one line
first_name1, last_name1, never_gonna_give_u_up, never_gonna_let_u_down, never_gonna_run_around, desert_u = "Rick", "Astley", True, True, True, False

#Exercises: Level 2
#Points 1-3
print("Variable 'first_name' is an ", type(first_name), ".")
print("Variable 'age' is an ", type(age), ".")
print("Variable 'is_light_on' is an ", type(is_light_on), ".")

print("Variable 'first_name1' is an ", type(first_name1), "with a lenght of", len(first_name1), ".")
print("Variable 'last_name1' is an ", type(last_name1), "with a lenght of", len(last_name1), ".")

if len(first_name1) > len(last_name1):
    print("The first name is longer than the last name.")
elif len(first_name1) == len(last_name1):
    print("The first name is as long as  the last name.")
else:
    print("The last name is longer than the last name.")

#Point 4
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

#Point 5
import math
#radius = 30
radius = input("Radius: ")
area_of_circle = (float(radius)**2)*math.pi
circum_of_circle = float(radius)*2*math.pi
print("Area of circle is", area_of_circle, "and circumference is", circum_of_circle, ".")

#Point 6
irst_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name
country = input("Country: ")
city = input("City: ")
age = input("What's my agae again? ")
