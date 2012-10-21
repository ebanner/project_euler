import prime_module

def sieve(limit):
    limit += 1
    nums = list(range(limit))
    prime = [True]*limit

    # 0 and 1 are not prime
    prime[0],prime[1],prime[2] = False,False,True

    #print(nums)
    #print(prime)

    for num in range(2,limit):
        #print("num = {}".format(num))
        if not prime[num]:
            #print("{} has already been shown not to be prime".format(num))
            continue
        #if prime_module.prime_huh(num):
        #print("{} is prime, so cross off all multiples of it".format(num))
        for n in range(num+num, limit, num):
            #print("trying to cross off {}".format(n))
            prime[n] = False
            #print(prime)

    actual_primes = [2]

    for num in range(3,len(prime),2):
        if prime[num]:
            actual_primes.append(num)
            
    #print(nums)
    #print(prime)

    return actual_primes
