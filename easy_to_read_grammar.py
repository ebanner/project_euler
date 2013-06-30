if __name__ == '__main__':
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    specials = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    all_numbers = []

    for digit in digits:  # will count up 1-9
        all_numbers.append(digit)

    for teen in teens:  # will count up 10-19
        all_numbers.append(teen)

    offset = 0

    for special in specials:
        all_numbers.append(special)
        for digit in digits:
            all_numbers.append(special+'-'+digit)

    one_through_ninety_nine = all_numbers[:]
    HUNDRED = 'hundred'
    AND = 'and'
    offset = 0

    for digit in digits:
        all_numbers.append(digit+' '+HUNDRED)
        for number in one_through_ninety_nine:
            all_numbers.append(digit+' '+HUNDRED+' '+AND+' '+number)

    all_numbers.append('one'+' '+'thousand')

    for i in range(0,len(all_numbers)-5,5):
        print("{:<30} {:<30} {:<40} {:<50} {:<60}".format(all_numbers[i], all_numbers[i+1], all_numbers[i+2], all_numbers[i+3], all_numbers[i+4]))

    print(all_numbers[-1])

    total = 0

    for number in all_numbers:
        total += len(number)
