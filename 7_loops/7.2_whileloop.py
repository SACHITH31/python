'''
WHILE LOOP SYNTAX :
while CONDITION :
  BODY OF WHILE LOOP



here in while loop we don't know how many iterations are doing
'''

a = 10
while a <= 20 :
    print('sachith', a)
    a = a + 1 # y we are using  this assignment operator instead of uniary operator ? GOTO 8_increment.py FILE


#NESTED LOOP 
for i in range(1, 6) :
    for j in range(1, 11) :
        print(i, 'x', j, '=',  i * j)
    print('\n')