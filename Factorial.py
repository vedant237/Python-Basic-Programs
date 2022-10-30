#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VEDANT CHAUDHARI
#
# Created:     13-01-2022
# Copyright:   (c) VEDANT CHAUDHARI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num = int(input('Enter the Number :'))
f = 1
for items in range(1,num+1):
    f = f*items
print('Factorial of the Given Number is :',f)
