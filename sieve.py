# say we're trying to find the largest prime factor of 121
# we're only going to find primes up to sqrt(121)

import math

### Functions

def prime_huh(n):
    # determine if a number is prime
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True

def mark_off_as_composite(primes, i):
    # mark off all multiples of the prime number as composite
    for i in range(i+i, len(primes), i):
        primes[i] = False

### End Functions


SIZE = 17
SUM = 0

primes = [True]*SIZE  # holds a boolean for each number indicating compositness
# Assume every number is prime until you find a composite factor
# primes[2] = True, primes[3] = True, primes[4] = True, etc...
# [True, True, True, True, True, ..., sqrt(...)]
divisor = [None]*SIZE  # list of possible divisors
# [1, 2, 3, 4, 5, ..., sqrt(...)]
nums = [None]*SIZE     # list of all numbers we are going to check
# [1, 2, 3, 4, 5, ..., sqrt(...)]

for i in range(SIZE):
    nums[i] = i
    divisor[i] = i

# we know 0 & 1 are not primes
primes[0],primes[1] = False,False

# print out lists
#print("nums")
#print(nums)
#print("divisors")
#print(divisor)
#print("primes")
#print(primes)

# we already know 2 & 3 are composite, so include them in the count of known
# primes -- start the count at 2
count = 3

# mark off every even number in the sieve as composite
mark_off_as_composite(primes,2)

# now let's test to see if each one is composite
for i in range(4,SIZE):
    count += 1
    if (not primes[i]):
        # if composite, don't check to see if it's prime, go onto the next
        continue
    if prime_huh(nums[i]):
        # if we find it to be a prime, cross off every multiple of it in the
        # sieve
        mark_off_as_composite(primes, i)
        # increment count because we found another prime
        #SUM += nums[i]

#print("primes: {}".format(primes))

for i in range(1,SIZE):
    if (primes[i]):
        print(nums[i])
        SUM += nums[i]
        print("SUM = {}".format(SUM))

print("count = {}".format(count))
print("SUM = {}".format(SUM))
