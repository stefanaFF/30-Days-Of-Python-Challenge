#Exercises - Day 4
#Point 1
po1_words = ['Thirty', 'Days', 'Of', 'Python']
po1_result = ' '.join(po1_words)
print(po1_result)

#Point 2 - 8
po2_words = ['Coding', 'For' , 'All']
company = ' '.join(po2_words)
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Point 9 - Method 1
first_space = company.index(' ')
first_word = company[0:first_space:1]
print(first_word)

#Point 9 - Method 2
split_company = company.split()
print(split_company[0])

#Point 10
print(company.find('Coding'))
print(company.index('Coding'))
print("Coding" in company)

#Point 11
print(company.replace('Coding', 'Python'))

#Point 12 - Method 1
print(company.replace('All', 'Everyone'))

#Point 12 - Method 2
company_no_all = company.strip('All')
print(f'{company_no_all}Everyone')

#Point 13
print(split_company)

#Point 14
list_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(list_company.split(','))

#Point 15
print(company[0])

#Point 16
print(len(company)-1)


#Point 17
print(company[10])

#Point 18
pfe = "Python for everyone"
pfe = pfe.title()
pfe1=pfe[0]
pfe_cut_mark1 = pfe.index(" ")
pfe_cut1 = pfe[pfe_cut_mark1+1]
pfe_cut_mark2 = pfe.rindex(" ",pfe_cut_mark1+1)
pfe_cut2 = pfe[pfe_cut_mark2+1]
print("This is the abbreviation: %s%s%s" % (pfe1, pfe_cut1, pfe_cut2))

#Point 18 - With help from the internet
def pfe_abb(pfe):
    words = pfe.split()
    short = "".join(word[0] for word in words)
    return short

pfe = "Python for everyone"
pfe_abb_res = pfe_abb(pfe)
print(pfe_abb_res.upper())

#Point 19
cfa = "Coding For All"
cfa_abb_res = pfe_abb(cfa)
print(cfa_abb_res.upper())

#Point 20 
print(cfa.index("C"))

#Point 21 
print(cfa.index("F"))

#Point 22
print(cfa.rindex("l"))

#Point 23 - 27
sentence_string = "You cannot end a sentence with because because because is a conjunction"
sentence_sub_string = "because"
point23 = sentence_string.index(sentence_sub_string)
print(point23)
point24 = sentence_string.rindex(sentence_sub_string)
print(point24)
print(sentence_string[point23:point24+len(sentence_sub_string)])
#or
sentence_sub_string2 = "because because because"
start_point25 = sentence_string.index(sentence_sub_string2)
end_point25 = start_point25 + len(sentence_sub_string2)
print(sentence_string[start_point25:end_point25])

#Point 28
print(cfa.startswith("Coding"))

#Point 29
print(cfa.endswith("coding"))

#Point 30
cfa_space = '   Coding For All      '
print(cfa_space.strip(" "))

#Point 31
strg1 = "30DaysOfPython"
strg2 = "thirty_days_of_python"
print(strg1.isidentifier())
print(strg2.isidentifier())

#Point 32
library_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" - ".join(library_list))

#Point 33
print("I am enjoying this challenge.\nI just wonder what is next.")

#Point 34
print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

#Point 35
radius = 10
area = 3.14*radius**2
print("radius = %s" % radius)
print("area = 3.14 * radius ** 2")
print("The area of a circle with radius {} is {:.2f} meters square.".format(radius,area))

#Point 34
a = 8
b = 6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))
