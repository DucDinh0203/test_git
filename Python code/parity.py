def parity(lst):
    p = 0
    i = 0
    n = len(lst) - 1
    # the use invariant is p as a parity of lst 
    #LI: i should be at the start index of the list, p initialises at 0
    # assume the invariant holds at state of some iteration, if the element in the list is odd, p switch to not p. otherwise, it remains unchange. Meanwhile, we increment i at the end of the iteration, 
    # at the end of the algorithm, i = n +1. so the invariant tells us that p is the parity of the sum of the list in lst[1...n]= lst, as required.
    while i <= n:
        if lst[i] % 2 == 1:
            p = not p
        i += 1
    return p
    #ter: p will illustate the parity of the list whether is true or false when ending the loop

my_list = [1, 2, 3, 4, 5, 7]
print(parity([]))