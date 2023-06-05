#Exercises: Level 1
#Point 1-5

empty_tuple = ()
names_1 = ("Angela", "Meridith")
names_2 = ("Pam", "Jim", "Dwight")
names = names_1 + names_2
print(len(names))
names_3 = ("Michael", "Prison Mike")
names = names + names_3
print(names)


#Exercises: Level 2
#Point 1

person_1, person_2, person_3, person_4, person_5, person_6, person_7 = names
print(person_1)
print(person_2)
print(person_3)
print(person_4)
print(person_5)
print(person_6)
print(person_7)

#Point 2
fruits = ("apple", "pineapples")
vegetables = ("carrots", "potatoes", "jalapeno")
animal_products = ("milk", "eggs","meat")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

if len(food_stuff_lt)%2 != 0:
    print(food_stuff_lt[len(food_stuff_lt)//2])
else:
    print(food_stuff_lt[len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

#Point 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia is a nordic country.",'Estonia' in nordic_countries)
print("ICeland is a nordic country.",'Iceland' in nordic_countries)
