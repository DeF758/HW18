'''
Vector of Ordered Values
v.1.0
Gerasimchik D.Y.
QA2022
19.04.2023
'''


def check_sort_asc(ls):
    for index in range(len(ls) - 1):
        if ls[index] >= ls[index + 1]:
            return False
    return True


def check_sort_desc(ls):
    for index in range(len(ls) - 1):
        if ls[index] <= ls[index + 1]:
            return False
    return True


def check(ls):
    return check_sort_asc(ls) or check_sort_desc(ls)


def create_list(size):
    ls = []
    for position in range(size):
        ls.append(int(input(f"Enter a number for position №{position + 1}: ")))
    return ls


def main():
    size = int(input("Input size of list: "))
    ls = create_list(size)
    output(check(ls))


def output(ls):
    if ls:
        msg = "All elements are arranged in order."
    else:
        msg = "The elements are NOT arranged in an ordered fashion."
    print(msg)


def test():
    print(check([1, 2, 3, 4, 5, 6]))
    print(check([6, 5, 4, 3, 2, 1]))
    print(check([1, 7, 3, 4, 5, 6]))
    print(check([1, 3, 3, 4, 5, 6]))
    print(check([1, 2, 2, 3, 3, 2]))
    print(check([8, 8, 8, 8, 8, 8]))


if __name__ == '__main__':
    main()
    test()
