# Q6 Reverse Number

n = int(input("Enter Number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reverse =", rev)