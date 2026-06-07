## 💻 Exercises: Day 5

### Exercises: Level 1

'''1. Declare an empty list'''
list1 = []

'''2. Declare a list with more than 5 items'''
list2 = [1, 2, 3, 4, 5]

'''3. Find the length of your list'''
len(list2)

'''4. Get the first item, the middle item and the last item 
of the list'''
print(list2[0], list2[len(list2)//2], list2[-1])

'''5. Declare a list called mixed_data_types, 
put your(name, age, height, marital status, address)'''
mixed_data_types = ["lornanu", 21, 170.0, "single", "Ireland"]

'''6. Declare a list variable named it_companies and assign 
initial values Facebook, Google, Microsoft, Apple, IBM, 
Oracle and Amazon.'''
it_companies = ["Facebook", "Google", "Microsoft","Apple", "IBM", "Oracle", "Amazon"]

'''7. Print the list using print()'''
print(it_companies)

'''8. Print the number of companies in the list'''
print(len(it_companies))

'''9. Print the first, middle and last company'''
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

'''10. Print the list after modifying one of the companies'''
it_companies[0] = "Meta"
print(it_companies)

'''11. Add an IT company to it_companies'''
it_companies.append("Adobe")

'''12. Insert an IT company in the middle of the companies list'''
it_companies.insert(len(it_companies)//2, "Samsung")
print(it_companies)

'''13. Change one of the it_companies names to uppercase (IBM excluded!)'''
print(it_companies[0].upper())

'''14. Join the it_companies with a string '# '''
print(", ".join(it_companies))

'''15. Check if a certain company exists in the it_companies list.'''
print("IBM" in it_companies)

'''16. Sort the list using sort() method'''
print(it_companies.sort())

'''17. Reverse the list in descending order using reverse() method'''
print(it_companies.reverse())

'''18. Slice out the first 3 companies from the list'''
print(it_companies[3:])

'''19. Slice out the last 3 companies from the list'''
print(it_companies[:-3])

'''20. Slice out the middle IT company or companies from the list'''
print(it_companies)
print(it_companies[:len(it_companies)//2] + it_companies[len(it_companies)//2 +1 :])

'''21. Remove the first IT company from the list'''
del it_companies[0]
print(it_companies)

'''22. Remove the middle IT company or companies from the list'''
it_companies.pop(len(it_companies)//2)

'''23. Remove the last IT company from the list'''
it_companies.pop()

'''24. Remove all IT companies from the list'''
it_companies.clear()

'''25. Destroy the IT companies list'''
del it_companies

'''26. Join the following lists:'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_list = front_end + back_end

'''27. After joining the lists in question 26. 
Copy the joined list and assign it to a variable full_stack, 
then insert Python and SQL after Redux.'''
full_stack = full_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

### Exercises: Level 2

'''1. The following is a list of 10 students ages:'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

'''- Sort the list and find the min and max age'''
ages.sort()
print(ages)
youngest, oldest = ages[0], ages[-1]

'''- Add the min age and the max age again to the list'''
ages.extend([youngest, oldest])

'''- Find the median age (one middle item or two middle 
items divided by two)'''
###12 items so even
ages.sort()
print("the median age is", ages[len(ages)//2])

'''- Find the average age (sum of all items divided by their number )'''
avg_age = sum(ages)/len(ages)
print("the average age is", avg_age)

'''- Find the range of the ages (max minus min)'''
print("the range is", ages[-1] - ages[0])

'''- Compare the value of (min - average) and (max - average), use _abs()_ method'''
print(abs(ages[0]-avg_age) == abs(ages[-1]-avg_age))

'''1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)'''
from countries import countries

# Find the middle country(ies) in the countries list
if len(countries) % 2 == 0:
    print("2 middle countries:", countries[len(countries)//2 - 1], {countries[len(countries)//2]})
else:
    print("1 middle country:", countries[len(countries)//2])

'''2. Divide the countries list into two equal lists if it is even if not one more country for the first half.'''
if len(countries) % 2 == 0:
    countries1= countries[:len(countries)//2]
    countries2= countries[len(countries)//2:]
else:
    countries1= countries[:len(countries)//2 + 1]
    countries2= countries[len(countries)//2 + 1:]

'''3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
Unpack the first three countries and the rest as scandic countries.'''
Select_Countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
CA, RU, US, *scandic = Select_Countries
print(Select_Countries)
print(scandic)
print(CA)