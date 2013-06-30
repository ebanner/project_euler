def collatz(n, count):
    while (n != 1):
        count += 1
        if (n % 2 == 0):  # n is even
            n = int(n/2)
        else:
            n = 3*n+1

    return count

if __name__ == '__main__':
    NUM = 1000000
    max_count = 0

    for num in range(1,NUM):
        if (num % 1000 == 0):
            print("num = {}".format(num))
        count = collatz(num, 1)
        if (count > max_count):
            max_count = count
            longest_chain = [max_count, num]
