# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#Point 1-5

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Meta", "Company2", "Company3"])
it_companies.remove("Facebook")
print(it_companies)
it_companies.discard("Appl") #discard doesn't raise error if item not found
print(it_companies)

#Exercises: Level 2
#Point 1-7

print(A)
C = set(list(A) + list (B))
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
joined_set_1 = A | B
print("A union B:", joined_set_1)
joined_set_2 = B | A
print("B union A:", joined_set_2)
print(A.symmetric_difference(B))
del A, B

#Exercises: Level 3
#Point 1-3

len_age_lst = len(age)
age_set = set(age)
len_age_set = len(age_set)
if len_age_lst == len_age_set:
    print("Equal.")
elif len_age_lst > len_age_set:
    print("List is longer {} > {}.".format(len_age_lst, len_age_set))
else:
    print("Set is longer {} < {}.".format(len_age_lst, len_age_set))

string_1 = "This is text."
list_1 = ("ordered","changeable","allow duplicate")
tuple_1 = ["ordered ", "unchangeable", "allow_ uplicate"]
set_1 = {"unordered", "un-indexed", "unchangeable", "distinct elements"}
print(string_1)
print(list_1)
print(tuple_1)
print(set_1)

sentence = "I am a teacher and I love to inspire and teach people"
word_list = sentence.split()
print(word_list)
unique_word_list = set(word_list)
print(unique_word_list)
