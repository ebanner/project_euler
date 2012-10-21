import math

def proper_divisors(n):
    divisors = {}
    for divisor in range(1,int(math.sqrt(n))+1):
        if (n % divisor == 0):
            divisors[divisor] = int(n/divisor)
    return divisors

max_perimeter = 1000+1
max_P,max_count = 0,0

for P in range(10,max_perimeter):
    count = 0
    limit = int((1/6)*P)+1
    for r in range(1,limit):
        divisors = proper_divisors(r**2/2)
        for s,t in divisors.items():
            #print("s = {0}, t = {1}".format(s,t))
            x = r+s
            y = r+t
            z = r+s+t
            if x+y+z == P:
                print("{0}+{1}+{2} is a solution to P={3}".format(x,y,z,P))
                count += 1
            #print("pythagorean triple: {0}, {1}, {2}".format(x,y,z))
    print("perimeter {0} has {1} solutions".format(P,count))
    #input()
    if count > max_count:
        max_count = count
        max_P = P
        print("max P value is now {}".format(max_P))
