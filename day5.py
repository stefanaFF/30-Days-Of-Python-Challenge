#Exercises: Level 1
#Point 1 - 4
empty_list = []
lst = ["never","goona","give","you", "up"]
print(len(lst))
first_item = lst[0]
last_item = lst[-1]
middle_item = lst[round(float((len(lst)-1)/2),None)]
print(first_item, middle_item, last_item)

#Point 5
mixed_data_type = ["FF", 300, 0.16, True, "Next door to Alice"]

#Point 6 - 25
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[round(float((len(it_companies)-1)/2),None)],it_companies[-1])
it_companies[0] = "Meta"
print(it_companies) 
it_companies.append("Samsung")
print(it_companies)
it_companies.insert(round(float((len(it_companies)-1)/2),None), "Dell")
print(it_companies)
it_companies[-3] = it_companies[-3].upper()
print(it_companies)
it_companies_str='#;  '.join(it_companies)
print(it_companies_str)
print("Google" in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])

if int((len(it_companies)-1)%2) == 0:
    middle_it_comp = int((len(it_companies)-1)//2)
    print(it_companies[middle_it_comp])
else:
    middle_it_comp = int((len(it_companies)-1)//2)
    print(it_companies[middle_it_comp:middle_it_comp+1])

del it_companies[0]
print(it_companies)

if int((len(it_companies)-1)%2) == 0:
    middle_it_comp = int((len(it_companies)-1)//2)
    del it_companies[middle_it_comp]
    print(it_companies)
else:
    middle_it_comp = int((len(it_companies)-1)//2)
    del it_companies[middle_it_comp:middle_it_comp+1]
    print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
#print(it_companies) --Returns error

#Point 26 - 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)
full_stack = joined_list.copy()
insert_point = full_stack.index("Redux")
sub_lst = ["Python", "SQL"]
full_stack = full_stack[:insert_point+1]+sub_lst+full_stack[insert_point+1:]
print(full_stack)
