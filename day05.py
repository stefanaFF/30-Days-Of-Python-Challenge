#Exercises: Level 1
#Point 1 - 4
empty_list = []
lst = ["never","gonna","give","you", "up"]
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

#Exercises: Level 2
#Point 1

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ascend= sorted(ages)
descend = sorted(ages, reverse=True)
print(ascend)
print(descend)
print("Min age:", min(ages))
print("Max age:", max(ages))
if len(ascend)%2 != 0:
    print("Median age:", ascend[len(ascend)//2])
else:
    mid1 = ascend[len(ascend)//2-1]
    mid2 = ascend[len(ascend)//2]
    print("Median age:", int(round((mid1 + mid2)/2,0)))

ages_average = int(round(sum(ages)/len(ages),0))
print("Averange age:", ages_average)

print("Age range:", max(ages)-min(ages))

if len(ascend)%2 != 0:
    min_list = ascend[0:len(ascend)//2+1]
    max_list = ascend[len(ascend)//2:]
    print("Min list:", min_list)
    print("Max list:", max_list)
    min_average = abs(sum(min_list)/len(min_list))
    max_average = abs(sum(max_list)/len(max_list))
    print("Min average:", min_average)
    print("Max average:", max_average)
else:
    mid1 = ascend[len(ascend)//2-1]
    mid2 = ascend[len(ascend)//2]
    print("Median age:", int(round((mid1 + mid2)/2,0)))
    min_list = ascend[0:len(ascend)//2]
    max_list = ascend[len(ascend)//2:]
    print("Min list:", min_list)
    print("Max list:", max_list)
    min_average = abs(sum(min_list)/len(min_list))
    max_average = abs(sum(max_list)/len(max_list))
    print("Min average:", min_average)
    print("Max average:", max_average)

#Point 2
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

if len(countries)%2 != 0:
    print("Middle country:", countries[len(countries)//2])
else:
    mid_co1 = countries[len(countries)//2-1]
    mid_co2 = countries[len(countries)//2]
    print("Middle countries: {} and {}".format(mid_co1, mid_co2))

if len(countries)%2 != 0:
    print("First half:", countries[0:len(countries)//2])
    print("Second half:", countries[len(countries)//2+1:])
else:
   print("First half:", countries[0:len(countries)//2])
   print("Second half:", countries[len(countries)//2+1:])

#Point 3
other_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rs, usa, *scandic_countries = other_list
print(ch)
print(rs)
print(usa)
print(scandic_countries)
