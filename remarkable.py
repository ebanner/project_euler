import math

def prime_huh(n):
    # determine if a number is prime
    if (n == 1):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True

best_a = 0
best_b = 0
max_prime = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        fantastic = lambda n: n**2 + a*n + b
        #print("n^2 + {0}n + {1}".format(a,b))
        awesome = fantastic(n)
        while (awesome >= 0 and prime_huh(awesome)):
            #print("prime: {}".format(fantastic(n)))
            n += 1
            awesome = fantastic(n)
        if (n > max_prime):
            best_a = a
            best_b = b
            max_prime = n
