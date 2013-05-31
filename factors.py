import math

def factors(n):
    divisors = []
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors.append(divisor)
            if (divisor != math.sqrt(n)):
                divisors.append(int(n/divisor))
    return divisors

if __name__ == '__main__':
    triangular_numbers = []
    next_triangular_number = 0

    for n in range(1,20000):
        next_triangular_number = int((n*(n+1))/2)
        triangular_numbers.append(next_triangular_number)

    DESIRED_DIVISORS = 500

    for triangular_number in triangular_numbers:
        divisors = factors(triangular_number)
        number_of_divisors = len(divisors)
        print("{0} has {1} divisors".format(triangular_number, number_of_divisors))
        if (number_of_divisors > DESIRED_DIVISORS):
            print("{0} is the first triangular number to have at least {1} divisors".format(triangular_number, DESIRED_DIVISORS));
            break
