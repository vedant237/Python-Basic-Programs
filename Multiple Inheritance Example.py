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
