'''

v.1.0
Gerasimchik D.Y.
QA2022
06.04.2023
'''


def check_mirror(ls):
    num = len(ls) // 2
    for index in range(num):
        if ls[index] != ls[len(ls) - 1 - index]:
            return False

    return True


def test():
    print(check_mirror([1, 2, 3, 2, 1]))
    print(check_mirror([1, 2, 3, 3, 2, 1]))
    print(check_mirror([1, 4, 3, 2, 1]))


if __name__ == '__main__':
    test()
