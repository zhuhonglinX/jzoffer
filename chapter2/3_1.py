
def find_dup(lst):
    for i in range(len(lst)):
        while lst[i] != i:
            m = lst[i]
            if lst[m] == lst[i]:
                return m
            # swap number position i and m
            lst[i], lst[m] = lst[m], lst[i]




if __name__ == '__main__':
    lst = [2, 3, 1, 0, 2, 5, 3]
    print(find_dup(lst))
