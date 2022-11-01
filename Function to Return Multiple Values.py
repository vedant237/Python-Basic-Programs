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

def div_remainder(a,b):
    div = a//b
    remainder= a%b
    return div, remainder

d,r = div_remainder(100,9)
print('Division is',d, 'and Remainder is ',r)