if __name__ == '__main__':
    product = 2**30

    for i in range(1000-30):
        product = 2*int(str(product)[-10:])
