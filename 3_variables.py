'''
syntax of variable :
variable_name = value
'''

'''
Rules of variables are :
1. variable name should start with only characters or underscore
2. python is an case sensitive (ex: python is different from Python)
3. in python file name can be started with numbers also
'''

# creating a variable
first_variable = 10
print(first_variable)

#a,b,c = 10 #here a single value can't be assigned to multiple variables BUT ANOTHER METHOD IS THERE TO PERFORM SAME OPERATION i.e..,
a = b = c = 10
print(a)
print(b)
print(c)

a,b,c = 1,2,3 # but here we can assign multiple values to multiple variables which means i.e.., number_of_variables = number_of_values
print(a,b,c)

c = 1,2,3 #this can be done where output is (1,2,3)
print("Printing c value")
print(c)

#TO KNOW ABOUT THE MEMORY LOCATION IN PYTHON WE USE id(variable_name) 
a = 100
print(id(a))
a = 200
a = 'string'
b = "string"
print(id(a))
print(id(b))

#CASE SENSITIVE 
a = 'hello coder'
A = 'HELLO CODER'
print(a)
print(A)

#TO INDICATE THAT THE VARIABLE IS CONSTANT THEN WE WRITE THAT VARIABLE_NAME IN UPPERCASE,it's just an indication and we can modify that also
PI = 3.14
print(PI)