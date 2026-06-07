## 💻 Exercises: Day 9

### Exercises: Level 1

'''1. Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. Output:
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.'''

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else: print('You need', (18-age), 'more years to learn to drive.')

'''2. Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”)
to get the age as input. 
You can use a nested condition to print 'year' for 
1 year difference in age, 'years' for bigger differences, 
and a custom text if my_age = your_age. Output:
    Enter your age: 30
    You are 5 years older than me'''
    
my_age = 21
your_age = int(input('Enter your age: '))

if your_age > my_age:
    if your_age - my_age >1:
        print('You are', your_age - my_age, 'years older than me.')
    else: print('You are', your_age - my_age, 'year older than me.')

elif my_age > your_age:
    if my_age - your_age >1:
        print("I am", my_age - your_age, 'years older than you.')
    else: print("I am", my_age - your_age, 'year older than you.')
else:
    print('We are the same age!')

'''3. Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3'''

a = input('Please input the first number: ')
b = input('Please input the second number: ')

if a > b:
    print('a is greater than b')
elif a<b:
    print('a is less than b')
else:
    print('a is equal to b')

### Exercises: Level 2
'''1. Write a code which gives grade to students according to theirs scores:
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F'''

student_grade = int(input('Please enter your score: '))

if student_grade >= 90:
    print('Your score is an A.')
elif student_grade <90 and student_grade >=80:
    print('Your score is a B.')
elif student_grade <80 and student_grade >=70:
    print('Your score is a C.')
elif student_grade <70 and student_grade >=60:
    print('Your score is a D.')
else:
    print('Your score is an F.')


'''2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer'''

month = str(input('Please enter the month: '))
if month == 'September' or month == 'October' or month == 'November':
    print('It is Autumn.')
elif month == 'December' or month == 'January' or month == 'February':
    print('It is Winter.')
elif month == 'March' or month == 'April' or month == 'May':
    print('It is Spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('It is Summer.')


'''3. The following list contains some fruits:'''
fruits = ['banana', 'orange', 'mango', 'lemon']
'''If a fruit doesn't exist in the list add the fruit to the list and print 
the modified list. If the fruit exists print('That fruit already exist in the list')'''

fruit_input = input('Please input a fruit: ')
if fruit_input not in fruits:
    fruits.append(fruit_input)
else:
    print('That fruit already exists in the list.')


### Exercises: Level 3
''' 1. Here we have a person dictionary. Feel free to modify it!'''
person={
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 28,
    'country': 'Ireland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

'''* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.'''
if 'skills' in person:
    print(person.get('skills')[len(person.get('skills'))//2])
else:
    print('This person has no listed skills.')

'''* If a person skills has only JavaScript and React, print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
else print('unknown title') - for more accurate results more conditions can be nested!'''


skills = set(person.get("skills"))
print(skills)
if skills == {"JavaScript", "React"}:
    print("Frontend developer")
elif skills == {"Node", "Python", "MongoDB"}:
    print("Backend developer")
elif {"React", "Node", "MongoDB"}.issubset(skills):
    print("Fullstack developer")
else:
    print("Unknown title")


'''* If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.'''

if person['is_married'] == True and person['country']== 'Ireland':
    print(person.get('first_name'), 'lives in Ireland. They are married')



