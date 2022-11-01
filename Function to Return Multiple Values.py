def div_remainder(a,b):
    div = a//b
    remainder= a%b
    return div, remainder

d,r = div_remainder(100,9)
print('Division is',d, 'and Remainder is ',r)
