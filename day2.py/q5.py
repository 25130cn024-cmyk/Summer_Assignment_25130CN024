# Q5 Sum of Digits

n = int(input("Enter Number: "))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print("Sum =", sum)
