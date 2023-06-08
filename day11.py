import math

#Exercises: Level 1
#Point 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    sum = a + b
    return sum
print(add_two_numbers(3,4))

#Point 2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = round(math.pi * r *r,2)
    return area
print(area_of_circle(5))

#Point 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_numbers(*num):
    total = 0
    for number in num:
        total += number
    return total
print(add_all_numbers(3, 4, 5, 6, 7, 8))

#Point 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    farenheit = 0
    farenheit = (celsius * (9/5)) + 32
    return farenheit
print(convert_celsius_to_fahrenheit(33))

#Point 5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    autumn_month = ["September", "October", "November"]
    winter_month = ["December", "January", "February"]
    spring_month = ["March", "April", "May"]
    summer_month = ["June", "July", "August"]
    if month.title() in autumn_month:
        print("{} is in autumn.".format(month.title()))
    elif month.title() in winter_month:
        print("{} is in winter.".format(month.title()))
    elif month.title() in spring_month:
        print("{} is in spring.".format(month.title()))
    elif month.title() in summer_month:
        print("{} is in summer.".format(month.title()))
    else:
        print("{} is not a valid month.".format(month.title()))
check_season("January")

#Point 6 - Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
     slope = (y2 - y1)/(x2 - x1)
     return slope
print(calculate_slope(2,2,5,5))

#Point 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(co_a, co_b, co_c):
    discriminant = co_b**2 - 4*co_a*co_c
    if co_a == 0:
        print ("The value of the coeficeint 'a' cannot be zero.")
    elif discriminant > 0:
        var_x1 = round((-co_b + math.sqrt(discriminant))/(2*co_a),2)
        var_x2 = round((-co_b - math.sqrt(discriminant))/(2*co_a),2)
        print("For the quadration ecuation {}x**2 + {}x + {} = 0, 'x' can take the value {} or {}.".format(co_a, co_b, co_c, var_x1, var_x2))
        return var_x1, var_x2
    elif discriminant == 0:
        var_x = -co_b/(2*co_a)
        print("For the quadration ecuation {}x**2 + {}x + {} = 0, 'x' can take the value {}.".format(co_a, co_b, co_c, var_x))
        return var_x
    else: 
        real_part = -co_b/(2*co_a)
        imaginery_part = round(math.sqrt(abs(discriminant)),2)
        img_x1 = complex(real_part, imaginery_part)
        img_x2 = complex(real_part, -imaginery_part)
        print("For the quadration ecuation {}x**2 + {}x + {} = 0, 'x' can take the value {} or {}.".format(co_a, co_b, co_c, img_x1, img_x2))
        return img_x1, img_x2
solve_quadratic_eqn(2,5,1)

#Point 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in range(len(lst)):
        for letter in lst[i]:
            print(letter)
print_list(["never","gonna","give","you", "up"])

#Point 9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)):
        reversed_list.append(lst[len(lst)-1-i])
    print(reversed_list)
    return reversed_list
reverse_list(["never","gonna","let","you", "down"])

#Point 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capp_lst = []
    for i in range(len(lst)):
        capp_lst.append(lst[i].upper())
    return capp_lst
print(capitalize_list_items(["never","gonna","run","around","and","desert","you"]))

#Point 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(["never","gonna","make","you"], "cry"))

#Point 12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it..
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(["never","gonna","say","goodbye","rick"], "rick"))  

#Point 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    nr_sum = 0
    for i in range(num+1):
        nr_sum += i
    print("The sum of all numbers from 1 to {} is {}.".format(num,nr_sum))
    return nr_sum
sum_of_numbers(100)

#Point 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum_odd = 0
    for i in range(num+1):
        if i%2 != 0:
            sum_odd += i
    print("The sum of all odd numbers from 1 to {} is {}.".format(num,sum_odd))
    return sum_odd
sum_of_odds(100)

#Point 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sum_even = 0
    for i in range(num+1):
        if i%2 == 0:
            sum_even += i
    print("The sum of all even numbers from 1 to {} is {}.".format(num,sum_even))
    return sum_even
sum_of_even(100)

#Exercises: Level 2
#Point 1 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    if type(num) != int or num < 0:
        print("The number is not an integer or it is not positive.")
    else:
        count_even = 0
        count_odd = 0
        for i in range(num+1):
            if i%2 == 0:
                count_even += 1
            else:
                count_odd +=1
        print("The number of odds are {}.\nThe number of evens are {}.".format(count_odd, count_even))
        return count_even, count_odd
evens_and_odds(100)

#Point 2 - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num < 0:
        print("Cannot calculate the factorial of a negative number.")
    else:
        fact = 1
        for i in range(1,num+1):
            fact *= i
        print("{}! = {}".format(num,fact))
        return fact
factorial(5)

#Point 3 - Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if not param:
        print("Is empty.")
        return True
    else:
        print("Not empty.")
        return False
is_empty([])

#Point 4 - Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    print("The mean of {} is {}.".format(lst,sum(lst) / len(lst)))
    return sum(lst) / len(lst)
calculate_mean([1, 2, 3, 4, 5, 5, 1])

def calculate_median(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst)%2 != 0:
        mid = sorted_lst[len(sorted_lst)//2]
    else:
        mid = sorted_lst[len(sorted_lst)//2-1:len(sorted_lst)//2+1]
    print("The median of {} is {}.".format(lst,mid))
    return mid
calculate_median([1, 2, 3, 4, 5, 6])

def calculate_mode(lst):
    mode_count = {}
    max_count = 0
    modes = []
    for nr in lst:
        if nr in mode_count:
            mode_count[nr] += 1
        else:
            mode_count[nr] = 1
        if mode_count[nr] > max_count:
            max_count = mode_count[nr]
    for nr, count in mode_count.items():
        if count == max_count:
            modes.append(nr)
    if len(modes) == len(lst):
        print("In the list {} there are no modes.".format(lst))
        return []
    print("The modes for {} are {}.".format(lst, modes))
    return modes
calculate_mode([1,1,2,2,3])

def calculate_range(lst):
    print("The range of {} is {}.".format(lst,max(lst) - min(lst)))
    return max(lst)-min(lst)
calculate_range([1, 2, 3, 4, 5, 6])

def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diff = [(nr - mean) ** 2 for nr in lst]
    print("The variante of {} is {}.".format(lst,round(sum(squared_diff)/len(lst),3)))
    return sum(squared_diff)/len(lst)
calculate_variance([1, 2, 3, 4, 5, 6])

def calculate_std(lst):
    variance = calculate_variance(lst)
    std = math.sqrt(variance)
    print("The standard deviation of {} is {}.".format(lst,round(std,3)))
    return std
calculate_std([1, 2, 3, 4, 5, 6])
