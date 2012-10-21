def swap(perm, i, j):
    temp = perm[i]
    perm[i] = perm[j]
    perm[j] = temp

def permutation(perm,length,i,list_of_perms):
    if i == length-1:
        list_of_perms.append(perm)
    else:
        for j in range(i,len(perm)):
            swap(perm,i,j)
            permutation(perm[:],length,i+1,list_of_perms)
            swap(perm,i,j)

def permute(perm,list_of_perms):
    my_map = map(lambda e: str(e), perm)
    perm = [e for e in my_map]
    permutation(perm,len(perm),0,list_of_perms)
