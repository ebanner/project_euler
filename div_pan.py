from permute import permute

if __name__ == '__main__':
    perms = []
    permute([0,1,2,3,4,5,6,7,8,9],perms)
    nums = [0]*len(perms)

    for i,perm in enumerate(perms):
        nums[i] = ''.join(perm)

    total = 0

    for perm in nums:
        if int(perm[7:]) % 17 == 0 and int(perm[6:9]) % 13 == 0 and int(perm[5:8]) % 11 == 0 and int(perm[4:7]) % 7 == 0 and int(perm[3:6]) % 5 == 0 and int(perm[2:5]) % 3 == 0 and int(perm[1:4]) % 2 == 0:
            total += int(perm)

    print("total is {}".format(total))
