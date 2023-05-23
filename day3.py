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

#Point 8 (this seems like overkill)
x_zero = 0
y_zero = 0
slope_c = -2
x_intercept = round(float((y_zero - slope_c)/2),3)
y_intercept = round(float(2 * x_zero + slope_c),3)
print("x-intercept is: (%s, 0)" % x_intercept)
print("y-intercept is: (0, %s)" % y_intercept)
slope_m1 = round(((0 - slope_c)/x_intercept),3)
print("Slope is: %s " % slope_m1)

#Point 9
po1_pair = input("Enter coordinate pair for point 1 separated by comma: ")
list1 = po1_pair.split(",")
for i in range(len(list1)):
    list1[i] = float(list1[i])
po2_pair = input("Enter coordinate pair for point 2 separated by comma: ")
list2 = po2_pair.split(",")
for i in range(len(list2)):
    list2[i] = float(list2[i])
x1 = round(float(list1[0]),3)
y1 = round(float(list1[1]),3)
x2 = round(float(list2[0]),3)
y2 = round(float(list2[1]),3)
x_diff = x2-x1
y_diff = y2-y1
slope_m2 = round(y_diff/x_diff,3)
euc_dist = round(math.sqrt(y_diff**2 + x_diff**2),3)
print("Slope is: %s " % slope_m2)
print("Euclidian distance is: %s " % euc_dist)

#Point 10
if slope_m2 > slope_m1:
    print("The second slope is greater.")
elif slope_m2 == slope_m1:
    print("The slopes are equal.")
else:
    print("The first slope is greater.")

#Point 11
another_x_value = float(input("Enter the first magic number: "))
another_y_value = round(float(another_x_value**2 + 6*another_x_value + 9),3)
print("For x = %s, y = %s" % (another_x_value, another_y_value))
#the function is x**2 + 6*x + 9 == 0
eq_a = 1
eq_b = 6
eq_c = 9
eq_x1 = round(float((0 - eq_b + math.sqrt(eq_b**2 - 4*eq_a*eq_c))/2*eq_a),3)
eq_x2 = round(float((0 - eq_b - math.sqrt(eq_b**2 - 4*eq_a*eq_c))/2*eq_a),3)
if eq_x1 == eq_x2:
    print("In the following function y = %s*x**2 + %s*x + %s, y = 0 if x = %s" % (eq_a, eq_b, eq_c, eq_x1))
else:
    print("In the following function y = %s*x**2 + %s*x + %s, y = 0 if x = %s or x = %s" % (eq_a, eq_b, eq_c, eq_x1, eq_x2))

#Point 12
word1 = input("Enter the word \"python\": ")
word2 = input("Enter the word \"dragon\": ")
print("The 2 words equal in lenght and this is NOT a lie. And the opposite of this is:", not bool(len(word1) == len(word2)))

#Point 13
print("The word 'on' is found in both 'python' and 'dragon'. That is:", "on" in word1 and "on" in word2)

#Point 14
sentence = "I hope this course is not full of jargon"
word_search = "jargon"
print("The %s jargon is present in the sentence '%s'. This is:" % (word_search, sentence), word_search in sentence)

#Point 15
print("The word 'on' is found in both 'python' and 'dragon' and this not a lie. That is:", not("on" in word1 and "on" in word2))

#Point 16
len_word1=len(word1)
float_word1 = float(len_word1)
str_word1 = str(float_word1)
print("The converted converted lenght of the word \"%s\" is:" % word1, str_word1)

#Point 17
number_check = int(input("Enter number to check: "))
if number_check % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

#Point 18
print(7//3 == int(2.7))

#Point 19
print(type('10')==type(10))

#Point 20
print(int(float('9.8'))==10)

#Point 21
hours = float(input("Enter number of worked hours: "))
rate = float(input("Enter rate per hour in \N{euro sign}: "))
payment = round(hours*rate,3)
print("Payment is %s \N{euro sign}." % payment)

#Point 22
years_on_earth = int(input("Years you have lived: "))
second_on_earth = years_on_earth*365*24*3600
print("You have lived for roughly %s seconds." % second_on_earth)

#Point 23 - the internet has the answers
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
