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

captains = {'England':'Root','Australia':'Smith','India':'Dhoni'}

del(captains['India'])
print(captains)

captains.popitem()
print(captains)

captains.pop('England')
print(captains)