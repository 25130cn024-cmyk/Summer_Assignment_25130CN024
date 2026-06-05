#Decimal to Binary
n = int(input("Enter decimal number: "))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary =", binary)
