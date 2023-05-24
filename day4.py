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
