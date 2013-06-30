if __name__ == '__main__':
    sequence = []

    for a in range(2,100+1):
        print("a = {}".format(a))
        for b in range(2,100+1):
            exp = a**b
            if (not sequence.__contains__(exp)):
                sequence.append(exp)

    print(len(sequence))
