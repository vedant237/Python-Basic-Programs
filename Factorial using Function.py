def factorial(n):
    fact = 1
    for no in range(1,n+1):
        fact *= no

    return fact

print(factorial(5))
