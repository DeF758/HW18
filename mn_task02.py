'''
The Mirror Vector
v.1.0
Gerasimchik D.Y.
QA2022
19.04.2023
'''

from mn_task01 import create_list


def check_mirror(ls):
    if len(ls) < 2:
        return False

    num = len(ls) // 2
    for index in range(num):
        if ls[index] != ls[len(ls) - 1 - index]:
            return False

    return True


def main():
    ls = create_list()
    output(check_mirror(ls))


def output(ls):
    if ls:
        msg = "All elements are mirrored."
    else:
        msg = "The elements are NOT mirrored, or the array is too small."
    print(msg)


def test():
    print(check_mirror([1, 2, 3, 2, 1]))
    print(check_mirror([1, 2, 3, 3, 2, 1]))
    print(check_mirror([31, 32, 33, 33, 33, 32, 31]))
    print(check_mirror([1, 4, 3, 2, 1]))
    print(check_mirror([12, 23, 32, 21]))
    print(check_mirror([1, 2, 3, 1]))
    print(check_mirror([]))
    print(check_mirror([4, 5]))


if __name__ == '__main__':
    main()
    test()
