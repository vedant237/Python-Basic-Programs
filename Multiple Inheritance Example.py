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

class Employee :
    company = 'Infosys'
    code = 420

class Freelancer :
    company = 'Fiverr'
    level = 2

class Programmer(Freelancer,Employee):   #Priority order of parent is decided here
    name = 'Rohit'                       # The first written parent is given priority
                                         #Here it priority is to Freelancer
p = Programmer()
print(p.company)
