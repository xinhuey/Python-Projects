#To create a simple calculator
#Greeting the user
print("Welcome to Calculator :)")
operation = input('''
Please input the math operation you would like to use:
Press + for addition
Press - for subtraction
Press * for multiplication
Press / for division
''')
inpnum_1 = int(input('Please enter your first number: '))
inpnum_2 = int(input('Please enter your second number: '))

if operation == '+':
   print(inpnum_1 + inpnum_2)

elif operation == '-':
     print(inpnum_1 - inpnum_2)

elif operation == '*':
     print(inpnum_1 * inpnum_2)

elif operation == '/':
     print(inpnum_1 / inpnum_2)

else:
       print('You have not selected a valid operator, please try again.')
