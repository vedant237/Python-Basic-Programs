#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VEDANT CHAUDHARI
#
# Created:     23-12-2021
# Copyright:   (c) VEDANT CHAUDHARI 2021
# Licence:     <your licence>
#---------------------------------------------------------------------------

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

