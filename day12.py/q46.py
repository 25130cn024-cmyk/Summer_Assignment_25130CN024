# Armstrong Number

def armstrong(n):
    power = len(str(n))
    total = 0

    for digit in str(n):
        total += int(digit) ** power

    return total == n

n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")