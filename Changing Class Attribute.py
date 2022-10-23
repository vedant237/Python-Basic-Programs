class Employee:
    company = 'Google'


vedant = Employee()
print(vedant.company)

Employee.company = 'Microsoft'
print(vedant.company)
