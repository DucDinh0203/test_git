def parity(lst):
    p = 0
    i = 1
    n = len(lst) - 1
    while i <= n:
        if lst[i] % 2 == 1:
            p = not p
        i += 1
    return p

my_list = [1, 2, 3, 4, 5, 6]
print(parity(my_list))
