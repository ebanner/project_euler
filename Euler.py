import math

def proper_divisors(n):
    divisors = []
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors.append(divisor)
            if (divisor != math.sqrt(n) and divisor != 1):
                divisors.append(int(n/divisor))
    return divisors

def legit_divisors(n):
    divisors = []
    for divisor in range(2,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors.append(divisor)
            if (divisor != math.sqrt(n)):
                divisors.append(int(n/divisor))
            divisors.append(n)
    return divisors

def sum_elements(my_list):
    total = 0
    for element in my_list:
        total += element
    return total

def fact(n):
    if (n == 1):
        return 1
    else:  # n is greater than 1
        return n * fact(n-1)

def factors(n):
    divisors = []
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors.append(divisor)
            if (divisor != math.sqrt(n)):
                divisors.append(int(n/divisor))
    return divisors

def sieve(limit):
    limit += 1
    nums = list(range(limit))
    prime = [True]*limit

    # 0 and 1 are not prime
    prime[0],prime[1],prime[2] = False,False,True

    for num in range(2,limit):
        if not prime[num]:
            continue
        for n in range(num+num, limit, num):
            prime[n] = False

    actual_primes = [2]

    for num in range(3,len(prime),2):
        if prime[num]:
            actual_primes.append(num)

    return actual_primes

def odd_composites(limit):
    """Instead of returning a list of primes, this returns a list of composits"""
    limit += 1
    nums = list(range(limit))
    # assume every number is prime
    prime = [True]*limit
    # 0 and 1 are not prime
    prime[0],prime[1],prime[2] = False,False,True

    for num in range(2,limit):
        if not prime[num]:
            continue
        for n in range(num+num, limit, num):
            prime[n] = False

    actual_primes = [2]
    odd_composites = []

    for num in range(3,len(prime),2):
        if not prime[num]:
            odd_composites.append(num)

    return odd_composites

def prime_factors(divisee):
    divisor,factors = 2,[]

    while divisee != 1:
        if divisee % divisor == 0:
            factors.append(divisor)
            divisee //= divisor
        else:
            divisor += 1

    return factors

def short_prime_factors(divisee):
    divisor,factors = 2,[]
    last_divisor = -1
    count = 0

    while divisee != 1:
        if count > 4:
            return []

        if divisee % divisor == 0:
            count += 1
            if divisor == last_divisor:
                factors[-1] *= divisor
            else:
                factors.append(divisor)
                last_divisor = divisor

            divisee //= divisor

        else:
            divisor += 1

    return factors
