import prime_module
import faster_eratosthenes

def left_to_right(n):
    """This function only tells you if a prime is left_to_right truncateable
    prime.  It assumes the number is already prime!"""
    #print("left to right for {}".format(n))
    if len(str(n)) == 1:
        if prime_module.prime_huh(n):
            return True
        else:
            return False
    elif prime_module.prime_huh(int(str(n)[1:])):
        return left_to_right(int(str(n)[1:]))
    else:
        return False

def right_to_left(n):
    """This function only tells you if a prime is right_to_left truncateable
    prime.  It assumes the number is already prime!"""
    #print("right to left for {}".format(n))
    if len(str(n)) == 1:
        if prime_module.prime_huh(n):
            return True
        else:
            return False
    elif prime_module.prime_huh(int(str(n)[:-1])):
        return left_to_right(int(str(n)[:-1]))
    else:
        return False

if __name__ == '__main__':
    NUM_PRIMES = 1000000
    print("right before getting {} primes".format(NUM_PRIMES))
    primes = faster_eratosthenes.sieve(NUM_PRIMES)
    truncateable_candidates = []

    for prime in primes:
        prime_string = str(prime)
        if not prime_string.__contains__('4') and not prime_string.__contains__('6') and not prime_string.__contains__('8'): 
            truncateable_candidates.append(prime)

    both = []

    for my_prime in truncateable_candidates:
        if left_to_right(my_prime) and right_to_left(my_prime):
            both.append(my_prime)

    both.remove(3)
    both.remove(5)
    both.remove(7)

    print(both)
