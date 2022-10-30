#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VISHWANATH CHAUDHARI
#
# Created:     13-03-2022
# Copyright:   (c) VISHWANATH CHAUDHARI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def factorial(n):
    fact = 1
    for no in range(1,n+1):
        fact *= no

    return fact

print(factorial(5))