comment = input('Enter the Comment :')

if('Subscribe Now' in comment ):
    spam = True
elif('Buy this Now' in comment):
    spam = True
elif('Click this Link' in comment):
    spam = True
else:
    spam = False


if(spam):
    print('This is a Spam Comment')
else:
    print('This is Not a Spam Comment')
