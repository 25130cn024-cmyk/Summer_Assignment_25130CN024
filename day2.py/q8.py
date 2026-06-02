# Q8 Palindrome Number

n = int(input("Enter Number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")