### Exercises: Day 8

'''1. Create  an empty dictionary called dog'''
dog = {}
print(type(dog))

'''2. Add name, color, breed, legs, age to the dog dictionary'''
dog['name'] = 'Ginger'
dog['colour'] = 'brown'
dog['breed'] = 'Yorkshire Terrier'
dog['legs'] = 4
dog['age'] = 16

'''3. Create a student dictionary and add first_name, last_name, gender, 
age, marital status, skills, country, city and address as keys for the dictionary'''
student = {'first_name' : 'Hayley',
           'last_name' : 'Williams',
           'gender' : 'Female',
           'age' : 21,
           'marital_status': 'single',
           'skills': ['Python','Research', 'Singing', 'Dancing'],
          'country': 'USA',
           'city': 'Nashville',
            'address': 'N/A' }

'''4. Get the length of the student dictionary'''
print(len(student))

'''5. Get the value of skills and check the data type, it should be a list'''
print(student.get('skills'))
print(type(student['skills']))

'''6. Modify the skills values by adding one or two skills'''
student['skills'].append(['Debating', 'Tennis'])
print(student['skills'])

'''7. Get the dictionary keys as a list'''
print(student.keys())

'''8. Get the dictionary values as a list'''
print(student.values())

'''9. Change the dictionary to a list of tuples using _items()_ method'''
print(student.items())

'''10. Delete one of the items in the dictionary'''
del student['marital_status']

'''11. Delete one of the dictionaries'''
del dog