if __name__ == '__main__':
    big_ass_string = ""

    for i in range(1000000):
        big_ass_string += str(i)

    total = 1
    d = 1
    while d < 1000001:
        total *= int(big_ass_string[d])
        d *= 10
