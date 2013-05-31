import math

def prime_huh(n):
    # determine if a number is prime
    if (n < 2):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True
