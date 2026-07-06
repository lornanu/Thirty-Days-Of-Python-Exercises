countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Exercises: Level 1
from functools import reduce

#1. Explain the difference between map, filter, and reduce.
'''The map function applies the function to every item in an iterable
Filter only selects items in an interable that meet a given requirement e.g. x < 10
Reduce performs the function step by step, element by element, and returns a singular final value.'''
#2. Explain the difference between higher order function, closure and decorator
''' A higher order function is a function that can be used with other functions, e.g. as a parameter.
Closure is a nested function where a function is defined inside of another function 
- the inner function remembers and uses variables from the outer function even when outer exits.

A decorator extends other functions without modifying the original function '''

#3. Define a call function before map, filter or reduce, see examples.
lst = [1,4,6,7,9]
def halfof(x):
    return x/2
list_halved = list(map(halfof, lst))
print(list_halved)

###
pvalues = [0.1,0.01,0.05,0.045, 0.003]
def issignificant(x):
    if x <0.05:
        return True
    else:
        return False
sigvals= list(filter(issignificant, pvalues))
print(sigvals)

###
def multiply_cumulatively(x, y):
    return x * y

print(reduce(multiply_cumulatively, numbers))

#4. Use for loop to print each country in the countries list.
for i in countries:
    print(i)

#5. Use for to print each name in the names list.
for i in names:
    print(i)
#6. Use for to print each number in the numbers list.
for i in numbers:
    print(i)

### Exercises: Level 2

#1. Use map to create a new list by changing each country to uppercase in the countries list
upper_list = list(map(lambda x: x.upper(), countries))
print(upper_list)

#2. Use map to create a new list by changing each number to its square in the numbers list
squared_list = list(map(lambda x: x**2, numbers))
print(squared_list)

#3. Use map to change each name to uppercase in the names list
lower_names = map(lambda x: x.lower(), names)
print(list(lower_names))

#4. Use filter to filter out countries containing 'land'.
def nolandcountries(country):
    if 'land' in country:
        return False
    else:
        return True
print(list(filter(nolandcountries, countries)))


#5. Use filter to filter out countries having exactly six characters.
def nosixcharas(country):
    if len(country) == 6:
        return False
    else:
        return True
print(list(filter(nosixcharas, countries)))

#6. Use filter to filter out countries containing six letters and more in the country list.
def nosixcharas(country):
    if len(country) >= 6:
        return False
    else:
        return True
print(list(filter(nosixcharas, countries)))

#7. Use filter to filter out countries starting with an 'E'
print(list(filter(lambda x: x[0] !='E', countries)))

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
upper_list_no_land = list(map(lambda x: x.upper(), filter(lambda x: 'land' not in x, countries)))
print(upper_list_no_land)

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    stringlist = map(lambda x: str(x), lst)
    return list(stringlist)

lst1= [2.0, 10, 'Italy', True]
print(get_string_lists(lst1))

#10. Use reduce to sum all the numbers in the numbers list.
def sum_nums(lst):
    return reduce(lambda x, y: x+y, numbers)

print(sum_nums(numbers))

#11. Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
result = reduce(lambda x, y: f"{x}, {y}", countries) + " are north European countries"
print(result)


#12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries

def countries_end_in_a(country_list):
    return (list(filter(lambda x: x[-1] is "a", country_list)))

print(countries_end_in_a(countries))

def countries_multiple_words(country_list):
    return (list(filter(lambda x: " " in x or "-" in x, country_list)))

print(countries_multiple_words(countries))

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_letter_frequency(country_list):
    dict_country = {}
    for country in country_list:
        first_letter = country[0]
        dict_country[first_letter] = dict_country.get(first_letter, 0) + 1
    return dict_country

print(country_letter_frequency(countries))

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(country_list):
    return country_list[:10]
print(get_first_ten_countries(countries))

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.#
def get_last_ten_countries(country_list):
    return country_list[-10:]
print(get_last_ten_countries(countries))


# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
import countries_data as c_data
#1. Sort countries by name, by capital, by population

#2. Sort out the ten most spoken languages by location.

#3. Sort out the ten most populated countries.