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
