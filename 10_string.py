# collection of characters is called STRING
'''
WE CAN DEFINE A STRING IN 3 TYPES THOSE ARE :
1.SINGLE QUOTES (' ')
2.DOUBLE QUOTES (" ")
3.THRIPLE QUOTES (''' ''')
'''

'''
METHODS IN STRING ARE :
1.lower()
2.upper()
3.endswith()
4.startswith()
5.replace("old_string", "new_string")
6.split()   #if we want to convert a string into a list then we use this split
7.count()
8.Rstrip()
9.Lstrip()
10.strip()  #it's like a trim in javascript 
11.removeprefix() #removes front part
12.removesuffix() #removes back part
13.index() 
14.find()
# the main difference between the index and find is when we want to find the index of a not presented element in collection by using index then we get an error message but if we use find for same condition it won't return error instead it returns -1
'''

a = 'sachith'
b = "sachith"
c = '''sachith'''
print(type(a),type(b),type(c))

'''
THE MAIN DIFFERNECE BETWEEN THE  'THRIPLE QUOTES FOR MULTI-LINE-STRINGS'  AND 'THRIPLE QUOTES FOR MULTI-LINE-COMMENTS' IS :

THRIPLE QUOTES FOR MULTI-LINE-STRINGS  :Triple quotes are mainly used to define strings that take up more than one line.
THRIPLE QUOTES FOR MULTI-LINE-COMMENTS :But remember, they(TRIPLE QUOTES) are not actually comments in Python. They are strings that are ignored by Python if not assigned to a variable.

'''

