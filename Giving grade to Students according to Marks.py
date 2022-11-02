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


c1 = float(input('Enter the Marks of Course 1 :'))
c2 = float(input('Enter the Marks of Course 2 :'))
c3 = float(input('Enter the Marks of Course 3 :'))
c4 = float(input('Enter the Marks of Course 4 :'))
c5 = float(input('Enter the Marks of Course 5 :'))

aggregate = ((c1 + c2 + c3 + c4 + c5)/500)*100

if(c1< 40 or c2< 40 or c3< 40 or c4< 40 or c5< 40):
    print('The Student is Fail because the Student got less than 40% in one of the Course')

elif(aggregate>75):
    print('The Student got Distinction Grade')

elif(60>=aggregate<75):
    print('The Student got First Grade')

elif(50>=aggregate<60):
     print('The Student got Second Grade'
elif(40>=aggregate<50):
     print('The Student got Third Grade')

else:
    print('''The Student is Fail because Student's Aggregate is Less than 40''')

