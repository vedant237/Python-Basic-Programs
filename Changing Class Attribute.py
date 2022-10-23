#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VISHWANATH CHAUDHARI
#
# Created:     22-01-2022
# Copyright:   (c) VISHWANATH CHAUDHARI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee:
    company = 'Google'


vedant = Employee()
print(vedant.company)

Employee.company = 'Microsoft'
print(vedant.company)