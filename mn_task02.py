'''
The Mirror Vector
v.1.0
Gerasimchik D.Y.
QA2022
06.04.2023
'''

from mn_task01 import create_list


def check_mirror(ls):
    num = len(ls) // 2
    for index in range(num):
        if ls[index] != ls[len(ls) - 1 - index]:
            return False

    return True


def main():
    size = int(input("Input size of list: "))
    ls = create_list(size)
    output(check_mirror(ls))


def output(ls):
    if ls:
        msg = "All elements are mirrored."
    else:
        msg = "The elements are NOT mirrored."
    print(msg)


def test():
    print(check_mirror([1, 2, 3, 2, 1]))
    print(check_mirror([1, 2, 3, 3, 2, 1]))
    print(check_mirror([31, 32, 33, 33, 33, 32, 31]))
    print(check_mirror([1, 4, 3, 2, 1]))
    print(check_mirror([12, 23, 32, 21]))
    print(check_mirror([1, 2, 3, 1]))


if __name__ == '__main__':
    main()
    test()
