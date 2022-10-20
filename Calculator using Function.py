def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def remainder(a,b):
    return a%b

def square(a):
    return a*a

num1 = int(input('Enter the First Number: '))
num2 = int(input('Enter the Second Number: '))

print('Enter the Choice /n1 1) Addition /n2 2) Subtraction /n3 3) Multiplication /n4 4) Division /n4 5) Remainder /n5 6) Square ')

choice = int(input())

if choice == 1:
    result = addition(num1,num2)
    print('Result is :',result)

elif choice == 2:
    result = subtraction(num1,num2)
    print('Result is :',result)

elif choice == 3:
    result = multiplication(num1,num2)
    print('Result is :',result)

elif choice == 4:
    result = division(num1,num2)
    print('Result is :',result)

elif choice == 5:
    result = remainder(num1,num2)
    print('Result is :',result)

elif choice == 6:
    result1 = square(num1)
    result2 = square(num2)
    print('Result 1 is ',result1 , ',Result 2 is',result2)

else:
    print('Please Enter Valid Choice !')
