captains = {'England':'Root','Australia':'Smith','India':'Dhoni'}

del(captains['India'])
print(captains)

captains.popitem()
print(captains)

captains.pop('England')
print(captains)
