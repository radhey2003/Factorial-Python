#This is a factorial finding file
a=int(input())

def factorial(a):
    if a ==1:
        return 1
    elif a ==0:
        return 1
    else:
        return (a*factorial(a-1))
print(factorial(a))