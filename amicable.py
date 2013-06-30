import math

def proper_divisors(n):
    divisors = []
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors.append(divisor)
            if (divisor != math.sqrt(n) and divisor != 1):
                divisors.append(int(n/divisor))
    return divisors

def d(n):
    total = 0
    divisors = proper_divisors(n)
    for divisor in divisors:
        total += divisor
    return total

NUM = 10000

amicable = []

for a in range(1,NUM):
    b = d(a)
    if (d(b) == a and a != b):
        amicable.append(a)
        amicable.append(b)

    print("d({0}) = {1}".format(a, d(a)))

print(amicable)
