def parity(lst):
    p = 0
    i = 0
    n = len(lst) - 1
    # the use invariant is p as a parity of lst
    while i <= n:
        if lst[i] % 2 == 1:
            p = not p
            print(p)
        i += 1
    return p

my_list = [1, 2, 3, 4, 5, 6]
print(parity(my_list))
print(not 0)