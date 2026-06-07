# Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1
'''1. Find the length of the set it_companies'''
len(it_companies)

'''2. Add 'Twitter' to it_companies'''
it_companies.add('Twitter')

'''3. Insert multiple IT companies at once to the set it_companies'''
it_companies.update(['Company1', 'Company2', 'Company3'])

'''4. Remove one of the companies from the set it_companies'''
it_companies.remove('Oracle')

'''5. What is the difference between remove and discard'''
###Remove raises an error if the item is not found, while discard does not.

### Exercises: Level 2

'''1. Join A and B'''
print(A.union(B))

'''2. Find A intersection B'''
print(A.intersection(B))

'''3. Is A subset of B'''
print('Is A a subset of B? ', A.issubset(B))

'''4. Are A and B disjoint sets'''
print('Are A and B disjoint sets? ', A.isdisjoint(B))

'''5. Join A with B and B with A'''
C = A.union(B)
print(C)
D = B.union(A)
print(D)

'''6. What is the symmetric difference between A and B'''
print(A.symmetric_difference(B))

'''7. Delete the sets completely'''
del A, B

### Exercises: Level 3

'''1. Convert the ages to a set and compare the length of the list and the set, 
which one is bigger?'''
age_st = set(age)
print('Is age set larger than age list? ', len(age_st) > len(age))

'''2. Explain the difference between the following data types: string, list, tuple and set'''
###string is a form of text, list is an easily changeable form of ordered items
###tuples are immutable collections of items
###sets are unordered collections of items and do not allow for duplicate items.

'''3. 'I am a teacher and I love to inspire and teach people.'
How many unique words have been used in the sentence? Use the split methods 
and set to get the unique words.'''

sentence = 'I am a teacher and I love to inspire and teach people.'
unique_words = ((set(sentence.split())))
print('There are ', len(unique_words), 'unique words in this sentence:', unique_words)