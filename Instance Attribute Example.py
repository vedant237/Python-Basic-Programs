class Employee:
    company = 'Google'
    salary = 100000

vedant = Employee()
vedant.salary = 200000

aarush = Employee()

print(vedant.salary)   #Showing working of Instance Attribute
print(aarush.salary)
print(vedant.company)
print(aarush.company)
