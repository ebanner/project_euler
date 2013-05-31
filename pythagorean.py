if __name__ == '__main__':
    a, b, c = 0, 1, 2
    a_val = b_val = c_val = 0

    while (a < 1000):
        while (b < 1000):
            while (c < 1000):
                if (a + b + c == 1000 and a**2 + b**2 == c**2):
                    a_val = a
                    b_val = b
                    c_val = c
                c += 1
            b += 1
            c = b+1
        a += 1
        b = a+1
        c = b+1
        print("a = {}".format(a))

    print("a = {}".format(a_val))
    print("b = {}".format(b_val))
    print("c = {}".format(c_val))
