'''
List : List used to store mutliple items in a single variable.
* It is an mutable which means we can modify the data.
* A List can have heterogeneous which can contain differnet types of data types.

LIST DECLARATION :
1. variable_name = [element1, element2, ......, element n]
2. variable_name = list((element1, element2, ......, element n))

* In List we can allow duplicates also.

** split(start:stop:skip)

List Methods: 
1.append()
2.extend()
3.remove()
4.insert(position, 'element')
5.pop(here we can give a particular element to remove from the list...         if we won't give anything then it removes the last element from the list)
6.clear() #it removes all the elements from  the  list 
7.count(element)
8.sort()
9.reverse()
10.copy()
11.del()
12.index(element) 
'''

a = [1,2,3,True, 1+3j, 'python', [11,22, [33,44]]]
# print(type(a))

b = list((1,2,3,5))
# print(b, type(b))

# print(a[6][2][1]) #accessing the elements through indexing 

# for i in a[::-1]:
#     print(i)

a[0] = 'sachith'
print(a)


a = [1,2,3,4,'a', 'python']

# a.append('sachithh')

a.extend(['sachith1', 'sachith2', 1])

a.remove('sachith1')

a.insert(0, 0)

a.pop(0)

# a.clear()

b = a.count(1)
# print(b)

c = [1,2,44,5,6,7,888,99]
c.sort() # here we should not assign this line to any variable bcz it doesn't returns anything so if we do then we get None as output.. EX: d = c.sort() here the output is None bcz it doesn't returns anything
c.reverse()
print(c)

d = [1,2,3,4,'sachith']
e = d.index('sachith')
print(e)

'''
LIST COMPREHENSION :
SYNTAX: [expression CONDITION]
'''
#ex: 
squares = [x**2 for x in range(5)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

