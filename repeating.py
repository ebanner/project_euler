if __name__ == '__main__':
    dividends = list(range(2,1000))
    decimals = []
    difference = [1]
    repeating = []

    for dividend in dividends:
        divisor = 1
        decimals = []
        difference = [1]
        while True:
            k = 0
            divisor *= 10
            while (dividend*(k+1) <= divisor):
                k += 1
            decimals.append(k)
            divisor = divisor - (dividend*k)
            if (difference.__contains__(divisor) or divisor == 0):  

                if (difference.__contains__(divisor)):  # if it's a repeating
                    decimals.append('*')
                    difference = [divisor]
                    while True:
                        k = 0
                        divisor *= 10
                        while (dividend*(k+1) <= divisor):
                            k += 1
                        decimals.append(k)
                        divisor = divisor - (dividend*k)
                        if (difference.__contains__(divisor) or divisor == 0):  
                            break
                        difference.append(divisor)
                repeating.append(decimals)
                break 

            difference.append(divisor)
        print("{0}/{1} = {2}".format(1, dividend, decimals))

    true_repeats = []

    for repeat in repeating:
        temp_repeat = []
        past_star = False
        for i in range(len(repeat)):
            if (past_star == False and repeat[i] != '*'):
                continue
            else:
                if (past_star == False): 
                    past_star = True
                    continue
                temp_repeat.append(repeat[i])
        true_repeats.append(temp_repeat)

    max_length = 0
    max_repeat = []
    d = 2
    big_d = 0

    for true_repeat in true_repeats:
        if (len(true_repeat) > max_length):
            max_length = len(true_repeat)
            max_repeat = true_repeat
            big_d = d
        d += 1
