def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return None

def find_min(lst, index):
    min_number = lst[index]
    start = index
    for i in range(index, len(lst)):
        if min_number > lst[i]:
            min_number = lst[i]
            start = i
    return start


# selection sort
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return None

# Task 2
def swap_down(lst, j):
    if lst[j] < lst[j - 1] and j > 0:
        lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return None


def shuffle_down(lst, k):
    marker = lst[k]
    j = k
    while j > 0 and lst[j - 1] > marker:
        lst[j - 1], lst[j] = lst[j], lst[j - 1]
        j -= 1
    return None


def insertion_sort(lst):
    for i in range(1, len(lst)):
        marker = lst[i]
        j = i
        while j > 0 and lst[j-1] > marker:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = marker
    return None


# Task 3
def degree(graph, v):
    count = 0
    for i in range(len(graph)):
        if graph[v][i] == 1:
            count += 1
    return count


def shared_friends(graph, u, v):
    friend_list = []
    for i in range(len(graph)):
        if graph[u][i] == graph[v][i] == 1:
            friend_list.append(i)
    return friend_list


def are_friends(graph, u, v):
    return graph[u][v] == 1


def clique(graph, vertices):
    check_friend_list = []
    for i in vertices:
        for j in vertices:
            if i != j:
                check = are_friends(graph, i, j)
                check_friend_list.append(check)
    if all(check_friend_list):
        return True
    else:
        return False