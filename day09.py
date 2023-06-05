#Exercises: Level 1
#Point 1
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Enter age.")

if age > 18:
    print("You are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive.".format(18-age))

print("You can leaglly vote.") if age > 18 else print("You need {} more years to legally vote.".format(18-age))

#Point 2
my_age = 42
while True:
    try:
        your_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Enter age.")

if my_age - your_age > 0:
    if my_age - your_age == 1:
        print("I am one year older than you.")
    elif your_age - my_age == 1:
        print("You are one year older than me.")
    else:
        print("I am {} years older than you.".format(my_age - your_age))
elif my_age == your_age:
    print("We are the same age.")
else:
    print("You are {} years older than me.".format(your_age - my_age))

#Point 3
while True:
    try:
        num1 = float(input("Enter number one: "))
        break
    except ValueError:
        print("Invalid input. Enter number.")

while True:
    try:
        num2 = float(input("Enter number two: "))
        break
    except ValueError:
        print("Invalid input. Enter number.")

if num1 == num2:
    print("The numbers are equal.")
elif num1 > num2:
    print("The first number (a={}) is greater than the second number (b={}).".format(num1, num2))
else:
    print("The second number (b={}) is greater than the first number (a={}).".format(num2,num1))

#Exercises: Level 2
#Point 1
while True:
    try:
        student_name = str(input("Enter stundent name: "))
        break
    except ValueError:
        print("Invalid input. Enter a name.")

while True:
    try:
        student_grade = int(input("Enter number one: "))
        break
    except ValueError:
        print("Invalid input. Enter a grade from 1 to 100.")

if student_grade < 50:
    print("{} with a score of {} has the grade F.".format(student_name, student_grade))
elif student_grade > 49 and student_grade < 60:
    print("{} with a score of {} has the grade D.".format(student_name, student_grade))
elif student_grade > 59 and student_grade < 70:
    print("{} with a score of {} has the grade C.".format(student_name, student_grade))
elif student_grade > 69 and student_grade < 80:
    print("{} with a score of {} has the grade B.".format(student_name, student_grade))
elif student_grade > 79 and student_grade < 101:
    print("{} with a score of {} has the grade A.".format(student_name, student_grade))
else:
    print("A student cannot not have a grade higher than 100.")

#Point 2
while True:
    try:
        month_name = str(input("Enter name of month: "))
        break
    except ValueError:
        print("Invalid input. Enter the name of the month.")
winter_month = ["December", "January", "February"]
spring_month = ["March", "April", "May"]
summer_month = ["June", "July", "August"]
autumn_month = ["September", "October", "November"]

if month_name in winter_month:
    print("The season is winter.")
elif month_name in spring_month:
    print("The season is spring.")
elif month_name in summer_month:
    print("The season is summer.")
elif month_name in autumn_month:
    print("The season is autumn.")
else:
    print("{} is not a valid month name.".format(month_name))

#Point 3
fruits = ['banana', 'orange', 'mango', 'lemon']
while True:
    try:
        fruit_name = str(input("Enter fruit name: "))
        break
    except ValueError:
        print("Invalid input. Enter the name of fruit.")

if fruit_name in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(fruit_name)
    print("The new fruit list is:", fruits)

#Exercises: Level 3
#Point 4

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 #Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    if len(person.get("skills"))%2 != 0:
        print("Middle: ", person["skills"][len(person.get("skills"))//2])
    else:
        print("Middle: ", person["skills"][len(person.get("skills"))//2-1:len(person.get("skills"))//2+1])
else:
    print("Key does not exist in dictionary.")

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if "Python" in person["skills"]:
        print("{} knows Python.".format(person["first_name"]))
    else:
        print("{} does not know Python.".format(person["first_name"]))
else:
    print("Key does not exist in dictionary.")

 #If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
 # - for more accurate results more conditions can be nested!
front_end = {"JavaScript", "React"}
back_end = {"Node", "Python", "MongoDB"}
fullstack = {"React", "Node", "MongoDB"}

if 'skills' in person:
    if set(person["skills"]) == front_end:
        print("The person is a front end developer.")
    elif set(person["skills"]).issuperset(back_end) == True and "React" not in person["skills"]:
        print("The person is a backend developer.")
    elif set(person["skills"]).issuperset(fullstack) == True:
        print("The person is a fullstack developer.")
    else:
        print("Unknown title.")
else:
    print("Key does not exist in dictionary.")

 #If the person is married and if he lives in Finland, print the information in the following format:
if person["is_married"] == True:
    print("{} from {} is married.".format(person["first_name"], person["country"]))
else:
    print("{} from {} is not married.".format(person["first_name"], person["country"]))
