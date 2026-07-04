## 💻 Exercises: Day 13

'''1. Filter only negative and zero in the list using list comprehension'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [i for i in numbers if i <=0]
print(negatives_and_zero)

'''2. Flatten the following list of lists of lists to a one dimensional list :'''
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
flattened = [n for row in list_of_lists for n in row]
print(flattened)

'''3. Using list comprehension create the following list of tuples:
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]'''
numbers_list = [(i, 1, i, i**2, i**3,i**4, i**5) for i in range(11)]
print(numbers_list)

'''4. Flatten the following list to a new list:'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

country_list = [[country[0].upper(), country[0].upper()[:3], country[1].upper()] for row in countries for country in row]
print(country_list)

'''5. Change the following list to a list of dictionaries:'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output: [{'country': 'FINLAND', 'city': 'HELSINKI'},{'country': 'SWEDEN', 'city': 'STOCKHOLM'},{'country': 'NORWAY', 'city': 'OSLO'}]'''
dictionary_country = [
    {'country': item[0].upper(), 'city': item[1].upper()}
    for country in countries #for each given country e.g. this has 3
    for item in country #for each item within that dictionary, e.g. item 1 and item 2
]
print(dictionary_country)

'''6. Change the following list of lists to a list of concatenated strings:'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   #output  ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
new_names = [f"{item[0]} {item[1]}"
             for name in names
             for item in name]
print(new_names)

'''7. Write a lambda function which can solve a slope or y-intercept of linear functions.'''
slope_calc = lambda y1, y2, x1, x2: (y2-y1)/(x2-x1)
print(slope_calc(1,2,3,4))

y_int = lambda y1, y2, x1, x2: y1 - slope_calc(y1,y2,x1,x2) * x1
#above is the calculation to find the y intercept

print(y_int(2,4,6,7))