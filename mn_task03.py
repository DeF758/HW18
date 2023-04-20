'''
Vector with the Same/Different Values
v.1.0
Gerasimchik D.Y.
QA2022
20.04.2023
'''


def check_all_the_same(ls):
    first = ls[0]

    for item in ls:
        if first != item:
            return False

    return True


def test():
    print(check_all_the_same([1, 1, 1]))
    print(check_all_the_same([1, 2, 1]))


if __name__ == '__main__':
    test()
