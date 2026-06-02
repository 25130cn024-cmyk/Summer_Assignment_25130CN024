# Q7 Product of Digits

n = int(input("Enter Number: "))
product = 1

while n > 0:
    product *= n % 10
    n //= 10

print("Product =", product)