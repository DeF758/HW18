'''

v.1.0
Gerasimchik D.Y.
QA2022
06.04.2023
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


def test():
    print(check([1, 2, 3, 4, 5, 6]))
    print(check([6, 5, 4, 3, 2, 1]))
    print(check([1, 7, 3, 4, 5, 6]))
    print(check([1, 3, 3, 4, 5, 6]))


if __name__ == '__main__':
    test()
