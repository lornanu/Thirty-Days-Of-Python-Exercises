## 💻 Exercises: Day 11

### Exercises: Level 1

'''1. Declare a function _add_two_numbers_. 
It takes two parameters and it returns a sum.'''
def add_two_numbers(x, y):
    return x + y
print(add_two_numbers(10, 5))

'''2. Area of a circle is calculated as follows: area = π x r x r. 
Write a function that calculates _area_of_circle_.'''

def area_of_circle(r, pi = 3.14):
    area = pi * r * r
    return area
print(area_of_circle(4))

'''3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
Check if all the list items are number types. 
If not do give a reasonable feedback.'''

def add_all_nums(*args):
    total = 0
    for arg in args:
        if type(arg) != int and type(arg) != float:
            return 'ERROR: Arguments must be numbers.'
    else:
        for num in args:
            total += num
    return total
print(add_all_nums(4,3,5,7, 'price'))


'''4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''

def convert_celcius_to_farenheit(C):
    return C * 9/5
print('the temperature in farenheit is:', convert_celcius_to_farenheit(120))

'''5. Write a function called check-season, it takes a month parameter and 
returns the season: Autumn, Winter, Spring or Summer.'''
def check_season(month):
    seasons= {
        'January':'Winter',
        'February':'Winter',
        'March':'Spring',
        'April':'Spring',
        'May':'Spring',
        'June':'Summer',
        'July':'Summer',
        'August':'Summer',
        'September':'Autumn',
        'October':'Autumn',
        'November':'Autumn',
        'December':'Winter',
    }
    if type(month) != str or month.capitalize() not in seasons:
        return "Argument must be a month."
    else:
        return seasons.get(month.capitalize())
print(check_season('april'))
print(check_season(5))

'''6. Write a function called calculate_slope which return the slope of a linear equation'''
def calculate_slope(x1, x2, y1, y2):
    m = (y2-y1)/(x2-x1)
    return m
print('The slope of the line is', calculate_slope(1,5,6,10))

'''7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
Write a function which calculates solution set of a quadratic equation,
 _solve_quadratic_eqn_.'''

def solve_quadratic_eqn(a,b,c):
    x1= (-b + (b**2 -4*a*c)**0.5)/2*a
    x2= (-b - (b**2 -4*a*c)**0.5)/2*a
    return('x= %s, and x= %s' % (x1, x2))
print('the two solutions for the quadratic equations are', solve_quadratic_eqn(1,-5,-6))


'''8. Declare a function named print_list. It takes a list as a parameter and 
it prints out each element of the list.'''

def print_list(lst):
    for item in lst:
        print(item)
lst= [1,4,6,7]
print_list(lst)

'''9. Declare a function named reverse_list. 
It takes an array as a parameter and it returns the reverse of the array (use loops).'''
def reverse_list(lst):
    reversed_list = []
    for item in range(len(lst) -1, -1, -1):
        reversed_list.append(lst[item])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 

'''10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

### Exercises: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
1. Write a function called _greet_ which takes a default argument, _name_. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```
1. Create a function called _show_args_ to take an arbitrary number of named arguments and print their names and values.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```


### Exercises: Level 3

1. Write a function called is_prime, which checks if a number is prime.
1. Write a functions which checks if all items are unique in the list.
1. Write a function which checks if all the items of the list are of the same data type.
1. Write a function which check if provided variable is a valid python variable
1. Go to the data folder and access the countries-data.py file.

- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.'''
