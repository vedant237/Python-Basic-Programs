First = input("Enter First Number : ")
Operator = input("Enter Operator (+,-,*,/,%) : ")
Second = input("Enter Second Number : ")

First=int(First)
Second=int(Second)

if Operator == "+":
    print(First + Second)
elif Operator == "-":
    print(First - Second)
elif Operator == "*":
    print(First * Second)
elif Operator == "/":
    print(First / Second)
elif Operator == "%":
    print(First % Second)
else: print('Invalid Operation !')

