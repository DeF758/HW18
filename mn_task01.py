'''
Vector of Ordered Values
v.1.0
Gerasimchik D.Y.
QA2022
19.04.2023
'''


def check_sort_asc(ls):
    if len(ls) < 2:
        return False

    for index in range(len(ls) - 1):
        if ls[index] >= ls[index + 1]:
            return False

    return True


def check_sort_desc(ls):
    if len(ls) < 2:
        return False

    for index in range(len(ls) - 1):
        if ls[index] <= ls[index + 1]:
            return False

    return True


def check(ls):
    return check_sort_asc(ls) or check_sort_desc(ls)


def create_list():
    size = int(input("Input size of list: "))
    ls = []

    for item in range(size):
        num = input(f"Enter a number for position №{item + 1}: ")

        while (not num.isdigit()):
            num = input(f"Oops! Invalid data. Try again..\n"
                        f"Enter a number for position №{item + 1}: ")
        else:
            ls.append(int(num))

    return ls


def main():
    ls = create_list()
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
    print(check([]))
    print(check([8]))
    print(check([8, 8]))


if __name__ == '__main__':
    main()
    test()
