#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VISHWANATH CHAUDHARI
#
# Created:     23-01-2022
# Copyright:   (c) VISHWANATH CHAUDHARI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee:
    company = 'Google'
    salary = 100000

vedant = Employee()
vedant.salary = 200000

aarush = Employee()

print(vedant.salary)   #Showing working of Instance Attribute
print(aarush.salary)
print(vedant.company)
print(aarush.company)