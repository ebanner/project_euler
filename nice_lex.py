import sys

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

permutations = []

count = 0

for digit1 in digits:
    for digit2 in digits:
        for digit3 in digits:
            for digit4 in digits:
                for digit5 in digits:
                    for digit6 in digits:
                        for digit7 in digits:
                            for digit8 in digits:
                                for digit9 in digits:
                                    for digit10 in digits:
                                        if (digit2 != digit1 and digit3 != digit2 and digit3 != digit1 and digit4 != digit3 and digit4 != digit2 and digit4 != digit1 and digit5 != digit4 and digit5 != digit3 and digit5 != digit2 and digit5 != digit1 and digit6 != digit5 and digit6 != digit4 and digit6 != digit3 and digit6 != digit2 and digit6 != digit1 and digit7 != digit6 and digit7 != digit5 and digit7 != digit4 and digit7 != digit3 and digit7 != digit2 and digit7 != digit1 and digit8 != digit7 and digit8 != digit6 and digit8 != digit5 and digit8 != digit4 and digit8 != digit3 and digit8 != digit2 and digit8 != digit1 and digit9 != digit8 and digit9 != digit7 and digit9 != digit6 and digit9 != digit5 and digit9 != digit4 and digit9 != digit3 and digit9 != digit2 and digit9 != digit1 and digit10 != digit9 and digit10 != digit8 and digit10 != digit7 and digit10 != digit6 and digit10 != digit5 and digit10 != digit4 and digit10 != digit3 and digit10 != digit2 and digit10 != digit1):
                                            permutations.append(digit1+digit2+digit3+digit4+digit5+digit6+digit7+digit8+digit9+digit10)
                                            print(permutations)
                                            count += 1
                                            print(count)
                                            if (len(permutations) == 1000000): 
                                                permutations.sort() 
                                                print(permutations[999999])
                                                sys.exit(0)

