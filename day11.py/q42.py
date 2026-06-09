# Maximum Number

def maximum(a, b):
    if a > b:
        return a
    return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))