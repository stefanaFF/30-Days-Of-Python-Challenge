# Day 1 - 30DaysOfPython Challenge

#Exercise: Level 1
#Point 2
print(3 + 4)             # addition(+)
print(4 - 3)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(4 / 3)             # division(/)
print(3 ** 4)            # exponential(**)
print(4 % 3)             # modulus(%)
print(4 // 3)            # Floor division operator(//)

#Point 3
print("FF"+" from Romania")
print("I am enjoying 30 days of python.")

#Point 4 - Checking data types
print(type(10))          # Int
print(type(9.8))         # Float
print(type(4 - 4j))      # Complex number
print(type('FF'))        # String
print(type([1, 2, 3]))   # List
print(type({'name':'FF'}))       # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


#Exercise: Level 2 (ish)
#Create directory
import os
parent_dir = "E://!!FF//30 - Python"
new_dir = "day_1"
path = os.path.join(parent_dir,new_dir)
try :
    os.mkdir(path)
    print("New folder '%s' created." % new_dir)
except OSError as error:
    print(error)

#Create file
file_name = "hellothere.py"
file_path = (path + "//" + file_name)
with open(file_path, 'w') as f:
    f.write("print(\"Aruba, Jamaica, ooh, I want to take ya to Bermuda, Bahama, come on, pretty mama\")\n")
    f.write("input()")
print("New file '%s' created." % file_name)


#Exercise: Level 3
#Point 2 - Euclidian Distance (line between 2 points)
#The first point has the coordinates (2,3) and the second point (10,8)
#The formula is d=sqrt((x1-x2)^2 + (y1-y^2)), sign doesn't matter since it's ^2.
import math

x1, y1 = input("Coordinates for the first point: ").split(",")
x2, y2 = input("Coordinates for the second point: ").split(",")
euc_dist = (math.sqrt((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2))
print (euc_dist)