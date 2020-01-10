#Sets
Sets = {}

#includes a data type for sets.
#curly braces or the set() function can be used to create sets.

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
# show that duplicates have been removed

# fast membership testing
'orange' in basket
'carbgrass' in basket

# demostrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a
# unique letters in a
a - b
#letters in a but not in b
a | b
#leters in a or b or both
a & b 
#letters in both a and b
a ^ b
#letters in a or b but not both

a - {x for x in 'abracadabra' if x not in 'abc'}
a

if  x in 'abc'
	for x in 'abracadabra'
print(x)

----------

fruits = {"apple","banana","cherry","orange","kiwi","melon","mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits






>>>Dictionaries
#dictionaries
#another useful data type built into python is the dictionary
tel = {'jack': 4098, 'sape': 4139
tel['jack']
tel['guido'] = 4127
tel


del tel['sape']
tel
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'sape' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}


#when looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)