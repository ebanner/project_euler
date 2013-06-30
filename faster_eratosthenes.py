import prime_module

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
