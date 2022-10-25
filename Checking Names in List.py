#-------------------------------------------------------------------------------
# Name:        Check whether Object is present in the List or Not.
# Purpose:
#
# Author:      VEDANT CHAUDHARI
#
# Created:     08-01-2022
# Copyright:   (c) VEDANT CHAUDHARI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

name = ['Vedant','Aarush','Vishwanath','Vaishali','Ram','Rahul','Raja','Rani']

find = input('Enter the Name to Check :')

if find in name :
    print('The given name is Present in the List')
else:
    print('The given name is not Present in the List')