# Exercises

'''1. Declare your age as integer variable'''
age = 21
'''2. Declare your height as a float variable'''
height = 200

'''3. Declare a variable that store a complex number'''
complex_n = 2 + 5j

"""4. Write a script that prompts the user to enter base and height 
of the triangle and calculate an area of this triangle 
(area = 0.5 x b x h)."""

base = float(input('Enter base:'))
height = float(input('Enter height:'))
area = 0.5 * base * height
print('the area of the triangle is', area)


'''5. Write a script that prompts the user to enter side a,
side b, and side c of the triangle. Calculate the perimeter of 
the triangle (perimeter = a + b + c).'''

a = float(input('Enter side a:'))
b = float(input('Enter side b:'))
c = float(input('Enter side c:'))
perimeter = a + b + c
print('the perimeter of the triangle is', perimeter)

'''6. Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) and 
perimeter (perimeter = 2 x (length + width))'''

rect_length = float((input('Enter length:')))
rect_width = float(input('Enter side width:'))

rect_area = rect_length * rect_width
rect_perimeter = 2*(rect_length+rect_width)
print('the area of the rectangle is', rect_area)
print('the perimeter of the rectangle is', rect_perimeter)


'''7. Get radius of a circle using prompt. 
Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.'''
c_radius = float(input('Enter circle radius:'))
c_area = 3.14 * c_radius**2
print('The area of the circle is:', c_area)
c_circumference = (2 * 3.14 * c_radius)
print('The circumference of the circle is:', c_circumference)

'''8. Calculate the slope, x-intercept and y-intercept of y = 2x -2'''
print("Slope = 2, x-intercept = 1, y-intercept = -2")


'''9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and 
point (6,10). '''
x1, y1, x2, y2 = 2, 2, 6, 10
m = (y2-y1)/(x2-x1)
print("slope is", m)
euclidean_distance = ((x2-x1)**2 + (y2-y2)**2)*0.5
print("euclidean distance is", euclidean_distance)

'''10. Compare the slopes in tasks 8 and 9.'''
print(2 == m)


'''11.Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is going to be 0.'''
### let y be 0
a, b, c = 1, 6, 9

quadratic_formula = (-b +- 0.5*(b**2 -4*a*c))/2*a
print(quadratic_formula)

'''12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.'''

print(len('python') != len('dragon)'))

'''13. Use an operator to check if 'on' is found in both 'python' and 'dragon'''
print('on' in 'python', 'on' in 'dragon')

'''14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.'''
print('jargon' in' I hope this course is not full of jargon.')

'''15.There is no 'on' in both dragon and python'''
print('on' not in 'dragon', 'on' not in 'python')

'''16. Find the length of the text python and convert the value to float and convert it to string'''
print(str(float(len('python'))))

'''17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a 
number is even or not using python?'''
print('number is even' if int(input("Enter integer: "))%2 == 0 else "number is odd")

'''18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.'''
7//3 == int(2.7)

'''19. Check if type of '10' is equal to type of 10'''
type('10') == type(10)


''' 20. Check if int('9.8') is equal to 10'''
int(9.8) == 10

''' 21. Write a script that prompts the user to enter hours and rate per hour. 
Calculate pay of the person?'''

rate = float(input('Enter the rate of pay:'))
hours = int(input('Enter the hours worked'))
pay = rate * hours
print('Your weekly earning is ',pay)

''' 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years'''
years = int(input('Please enter the number of years you have lived: '))
life = years * 365 * 24 * 60 * 60
print('You have lived for ', life, 'seconds.')


'''Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

## i would not have gotten this, loops not in today's lesson
