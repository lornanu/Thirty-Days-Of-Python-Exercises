###Exercises: Level 1
print('LEVEL 1')
'''1. Write a function which generates a six digit/character random_user_id.
  print(random_user_id()) 
  "1ee33d"'''

import random
import string
def random_user_id():
    charas = string.ascii_letters + string.digits #full range of numbers + letters
    user_id="" #empty string to add to
    for i in range(6):
       user_id += random.choice(charas) #build the ID string with random charas
    return user_id

print(random_user_id())

'''2. Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn't take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the 
number of IDs which are supposed to be generated.

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr'''

def user_id_gen_by_user():
    chara_count = int(input('enter number of characters: '))
    length = int(input('enter number of IDs desired: '))
    charas = string.ascii_letters + string.digits #full range of all numbers and letters
    for i in range(length):
      user_id="" #add random characters until ID reaches determined length
      for n in range(chara_count):
        user_id += random.choice(charas) #add a random character for the character count specified
      print(user_id)

user_id_gen_by_user()


'''3. Write a function named rgb_color_gen. 
It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
'''
from random import randint
def rgb_color_gen():
   a= randint(0,256)
   b= randint(0,256)
   c= randint(0,256)
   full = f"rgb({a},{b},{c})"
   return full

print(rgb_color_gen())

print('LEVEL 2')
###Exercises: Level 2
'''1.Write a function list_of_hexa_colors which returns any number of hexadecimal colors 
in an array (six hexadecimal numbers written after#. Hexadecimal numeral system is made out of 16 symbols, 
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).'''

def list_of_hexa_colours():
  charas = "0123456789abcdef" 
  rn = randint(0,10) #random number of hexa colours to produce
  hexa_list=[] #empty list to add to
  for i in range(rn):
    out='#'
    for p in range(6):
      out += random.choice(charas) #build each hexa color string
    hexa_list.append(out)
  return hexa_list
  
        
print(list_of_hexa_colours())

'''2.Write a function list_of_rgb_colors which returns any 
number of RGB colors in an array.'''

def list_of_rgb_colours():
   rgb_list=[]
   n= randint(0,10)
   for i in range(n):
      a= randint(0,256)
      b= randint(0,256)
      c= randint(0,256)
      rgb_list.append(f"rgb({a},{b},{c})")
   return rgb_list

print(list_of_rgb_colours())

'''3. Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']'''

def generate_colours(colourtype, nu):
    if  colourtype == 'rgb':
      rgb_list=[]
      for i in range(nu):
        a= randint(0,256)
        b= randint(0,256)
        c= randint(0,256)
        rgb_list.append(f"rgb({a},{b},{c})")
      return rgb_list
    elif colourtype == 'hexa':
        charas = "0123456789abcdef" 
        hexa_list=[] #empty list to add to
        for i in range(nu):
          out='#'
          for p in range(6):
            out += random.choice(charas) #build each hexa color string
          hexa_list.append(out)
        return hexa_list
    else:
       'error: please specify either "rgb" or "hexa" and use integers to determine the number of colours to generate, e.g. ("hexa", 3)'

print(generate_colours("hexa", 4))
print(generate_colours("rgb", 7))
       
print('LEVEL 3')
###Exercises: Level 3
'''1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list'''
def shuffle_list(lst):
  shuffled_lst = list.copy(lst)
  random.shuffle(shuffled_lst)
  print(shuffled_lst)

listint = [1,2,3,4,5,6]
liststr = ['apples', 'bananas', 'pears', 'coconuts']
shuffle_list(listint)
shuffle_list(liststr)
      

'''2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.'''
def seven_num():
  numlist = []
  numrange = [0,1,2,3,4,5,6,7,8,9]
  for i in range(7):
     num = random.choice(numrange)
     numlist.append(num)
     numrange.remove(num)
  return numlist

print(seven_num())
