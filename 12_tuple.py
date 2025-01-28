'''
Tuple : It is an ordered, immutable, collection of items .
* Once a tuple is created then it's values cannot be modified. Which makes differnent from the LIST.
* And we can store heterogenous types of data items in an tuple.
* Tuple allows the multiple occurences.

SYNTAX OF TUPLE: 
VARIABLE_NAME = (element1, element2, element3, ...., element n)
VARIABLE_NAME = tuple((element1, element2, element3, ...., element n))

'''

# accessing the elements from an TUPLE
a = (1,2,3,4,5)
print(a[1])
# accessing the last elements
print(a[-1])


# slicing the tuple
print(a[1: 4])


#Tuple concardination
a = (1,2,3)
b = (4,5,6)
print(a + b)
# Tuple repeatation 
print(a * 2)
# Tuple length
print(len(a))
# Tupel Iterating
for i in a:
    print(i)

'''
Tuple Packing and Unpacking:
Packing is when you assign multiple values to a tuple.
Unpacking is when you assign the tuple values to individual variables.

'''
# Packing
my_tuple = (10,20,30)
# Unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)

'''
Nested Tuples:
Tuples can contain other tuples as elements, which are called nested tuples.

'''
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  
print(nested_tuple[1][1])


'''
Tuple Methods:
Although tuples are immutable, there are a few methods you can use with them:

count(): Returns the number of occurrences of a specified value.
index(): Returns the index of the first occurrence of a specified value.

'''

my_tuple = (1, 2, 3, 2, 4, 2)
# count() method
print(my_tuple.count(2)) 
# index() method
print(my_tuple.index(3)) 


'''
Tuple with One Element:
To create a tuple with a single element, you need to add a comma after the element.

'''

single_element_tuple = (5,)  # Notice the comma!
print(single_element_tuple)  # Output: (5,)


'''
Nested Tuples:
Tuples can contain other tuples as elements, which are called nested tuples.

'''

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[1][1])  # Output: 4
