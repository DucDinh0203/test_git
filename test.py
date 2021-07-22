print("hello, world!")

def is_in(char, string):
    count = 0
    for i in string:
        if char == i:
            count += 1
    if count > 0:
        return True
    else:
        return False


def is_sorted(mylist):
    count = 0
    for i in range(0, len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            count = 1
    if count != 1:
        return True
    else:
        return False


def abs(x):
    if x < 0:
        return x * -1
    else:
        return x


def all(mylist):
    count = 0
    for i in mylist:
        if bool(i) == False:
            count = 1
    if count == 0:
        return True
    else:
        return False


def any(mylist):
    count = 0
    for i in mylist:
        if bool(i):
            count = 1
    if count == 1:
        return True
    else:
        return False


def max(mylist):
    big = mylist[0]
    for i in range(1, len(mylist)):
        if mylist[i] >= big:
            big = mylist[i]
            # print("big: ", big)
            # print(mylist[i])
    return big


def min(mylist):
    small = mylist[0]
    for i in range(1, len(mylist)):
        if mylist[i] <= small:
            small = mylist[i]
    return small


def reversed(mylist):
    l = len(mylist) - 1
    new_list = []
    while l >= 0:
        new_list.append(mylist[l])
        l -= 1
    return new_list


def sum(mylist):
    result = 0
    for i in mylist:
        result += i
    return result


def bin(x):
    i = 1
    b = 0
    if x < 0:
        x = x * (-1)
        while x > 0:
            reminder = x % 2
            b = b + (i * reminder)
            x = x // 2
            i *= 10
        return '-0b' + str(b)
    else:
        while x > 0:
            reminder = x % 2
            b = b + (i * reminder)
            x = x // 2
            i *= 10
        return '0b' + str(b)


def enumerate(mylist, start=0):
    new_list = []
    for i in range(0, len(mylist)):
        row = ()
        for j in range(0, 1):
            row = row + (start,)
            row = row + (mylist[i],)
        new_list.append(row)
        start += 1
    return new_list


def filter(function, mylist):
    new_list = []
    for i in mylist:
        if isinstance(function(i), int):
            if function(i):
                new_list.append(i)
        elif isinstance(i[0], char) and function(i[0]) == True:
            new_list.append(i)
    return new_list


def map(function, mylist):
    new_list = []
    for i in mylist:
        if isinstance(function(i), int):
            if isinstance(i, int):
                new_list.append(i * 2)
            else:
                new_list.append((i + i))
        else:
            new_list.append(function(i))
    return new_list


def lim_range(start, stop, step=1):
    mylist = []
    if step < 0:
        while start > stop:
            mylist.append(start)
            start += step
        return mylist
    else:
        while start < stop:
            mylist.append(start)
            start += step
        return mylist


def set(mylist):
    newlist = [] * 100
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist


def partition(mylist, low, high):
    pivot = mylist[high]
    i = low
    for j in range(low, high):
        if mylist[j] < pivot:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            i += 1
    mylist[i], mylist[high] = mylist[high], mylist[i]
    return i


def quickSort(mylist , low, high):
    if low < high:
        pi = partition( mylist, low, high)
        quickSort(mylist, low, pi - 1)
        quickSort(mylist, pi + 1, high)


def sorted(mylist):
    lst = list()
    if isinstance(mylist, str):
        for i in mylist:
            print(ord(i) - 96)
            lst.append( ord(i) - 96)
        quickSort(lst, 0, len(lst) - 1)
        res = list()
        for i in lst:
            res.append(chr(i + 96))
        return res
    quickSort(mylist, 0, len(mylist) - 1)
    return mylist