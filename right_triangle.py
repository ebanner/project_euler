import math

def proper_divisors(n):
    divisors = {}
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors[divisor] = int(n/divisor)
    return divisors

if __name__ == '__main__':
    max_perimeter = 1000+1
    max_P,max_count = 0,0

    for P in range(10,max_perimeter):
        count = 0
        limit = int((1/6)*P)+1
        for r in range(1,limit):
            divisors = proper_divisors(r**2/2)
            for s,t in divisors.items():
                x = r+s
                y = r+t
                z = r+s+t
                if x+y+z == P:
                    print("{0}+{1}+{2} is a solution to P={3}".format(x,y,z,P))
                    count += 1
        print("perimeter {0} has {1} solutions".format(P,count))
        if count > max_count:
            max_count = count
            max_P = P
            print("max P value is now {}".format(max_P))
