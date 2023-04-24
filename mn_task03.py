'''
Vector with the Same/Different Values
v.1.0
Gerasimchik D.Y.
QA2022
24.04.2023
'''
from mn_task01 import create_list


def check_all_the_same(ls):
    if len(ls) < 2:
        return False

    first = ls[0]
    for item in ls:
        if first != item:
            return False

    return True


def check_all_the_different(ls):
    if len(ls) < 2:
        return False

    for i in range(len(ls) - 1):
        for item in range(i + 1, len(ls)):
            if ls[i] == ls[item]:
                return False

    return True


def main():
    ls = create_list()
    same_digit = check_all_the_same(ls)
    different_digit = check_all_the_different(ls)
    output(same_digit, different_digit)


def output(same_digit, different_digit):
    if same_digit:
        msg = "All array elements are equal."
    elif different_digit:
        msg = "All array elements are distinct."
    else:
        msg = ("Array elements do not satisfy the condition, "
               "or the array is too small.")
    print(msg)


def test():
    same = str(check_all_the_same([8, 8, 8, 8]) == True) + "\n"
    same += str(check_all_the_same([8, 8, 6, 6]) == False) + "\n"
    same += str(check_all_the_same([]) == False) + "\n"
    same += str(check_all_the_same([-2, -2, -2, -2]) == True) + "\n"
    same += str(check_all_the_same([-2, -2, 2, 2]) == False)

    different = "\n\n" + str(check_all_the_different([1, 2, 3, 4]) == True) + "\n"
    different += str(check_all_the_different([2, 4, 6, 4]) == False) + "\n"
    different += str(check_all_the_different([]) == False) + "\n"
    different += str(check_all_the_different([-1, -3, -5, -7, -9]) == True) + "\n"
    different += str(check_all_the_different([-1, -3, -5, -7, 3]) == True) + "\n"

    print(same, different)


if __name__ == '__main__':
    main()
    test()
