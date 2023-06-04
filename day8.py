#Exercises: Day 8
#Point 1-2
dog = {}
dog ['name'] = 'Ollie'
dog ['color'] = 'chocolate'
dog ['breed'] = 'good boy'
dog ['legs'] = True
dog ['age'] = 42
print(dog)

#Point 3
student_dog = {'first_name':'Ollie',
           'last_name':'NibNib',
           'gender':'Boy Dog',
           'age': 42,
           'marital_status': False,
           'skills': ['beeing a good boy','nib nibs'],
           'country': 'Magic Country',
           'city': 'Magic City',
           'address': {'street':'Good Boy Avenue',
                       'number':1
           }
           }
print("Initial dictionary:\n",student_dog)

student_dog['skills'].append('mlem')

print(len(student_dog))
print("Skills:\n", student_dog.get('skills'))
print(type(student_dog.get('skills')))

sd_keys = student_dog.keys()
print("Keys:\n", list(sd_keys))
sd_values = student_dog.values()
print("Values\n:", list(sd_values))

print("Items:\n",student_dog.items())

student_dog.pop('marital_status')
del dog
print("Final dictionary:\n", student_dog)
