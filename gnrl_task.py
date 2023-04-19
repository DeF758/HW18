'''
Working with numbers in a list
v.1.0
Gerasimchik D.Y.
QA2022
16.04.2023
'''
from random import randint


def get_max_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] < ls[i]:
            index = i

    return index


def get_min_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] > ls[i]:
            index = i

    return index


def swap_extreme_elements(ls):
    max_index = get_max_value_index(ls)
    min_index = get_min_value_index(ls)
    ls[max_index], ls[min_index] = ls[min_index], ls[max_index]


def rand_init(ls, a=-50, b=50):
    for i in range(len(ls)):
        ls[i] = randint(a, b)


def counter_average(ls):
    average = 0
    for i in range(len(ls)):
        average += ls[i]
    average /= len(ls)

    return average


def convert(ls):
    msg = ""
    for item in ls:
        msg += str(item) + " "

    return msg


def counter_positive_dgts(ls):
    positive = 0
    for i in range(len(ls)):
        if 0 < ls[i]:
            positive += 1

    return positive


def counter_negative_dgts(ls):
    negative = 0
    for i in range(len(ls)):
        if 0 > ls[i]:
            negative += 1

    return negative


def counter_zero_dgts(ls):
    zero = 0
    for i in range(len(ls)):
        if 0 == ls[i]:
            zero += 1

    return zero


def create_list(size, value=0):
    ls = []
    for _ in range(size):
        ls.append(value)

    return ls


def main():
    size = int(input("Input size of list: "))
    ls = create_list(size)
    rand_init(ls)

    msg = f"Before: {convert(ls)}"
    print(msg)

    swap_extreme_elements(ls)
    msg = (f"After: {convert(ls)}"
           f"\nMax value is: {ls[get_max_value_index(ls)]}"
           f"\nMin value is: {ls[get_min_value_index(ls)]}"
           f"\nAverage is: {counter_average(ls)}"
           f"\nPositive digits: {counter_positive_dgts(ls)}"
           f"\nNegative digits: {counter_negative_dgts(ls)}"
           f"\nZero digits: {counter_zero_dgts(ls)}")
    print(msg)


def test():
    extreme = ("Max i[2] " +
               str(get_max_value_index([5, 66, 75, 34, 2, 8]) == 2))
    extreme += ("\nMax i[2] " +
                str(get_max_value_index([5, 66, 75, 75, 2, 8]) == 2))
    extreme += ("\nMax i[3] " +
                str(get_max_value_index([-5, -66, -75, -2, -8]) == 3))
    extreme += ("\nMin i[4] " +
                str(get_min_value_index([5, 66, 75, 34, 2, 8]) == 4))
    extreme += ("\nMin i[2] " +
                str(get_min_value_index([-5, -66, -75, -2, -8]) == 2))

    average = ("\n\nArithmetic mean of 3 " +
               str(counter_average([1, 2, 3, 4, 5]) == 3))
    average += ("\nArithmetic mean of 0 " +
                str(counter_average([0, 0, 0, 0, 0]) == 0))
    average += ("\nArithmetic mean of -3 " +
                str(counter_average([-1, -2, -3, -4, -5]) == -3))

    positive = ("\n\nPositive elements: 6 " +
                str(counter_positive_dgts([8, 6, 9, 4, 5, 6]) == 6))
    positive += ("\nPositive elements: 2 " +
                 str(counter_positive_dgts([-8, 6, 0, 9, -4, -5, -6, 0]) == 2))
    positive += ("\nPositive elements: 0 " +
                 str(counter_positive_dgts([-8, -6, 0, -9, -4, -5, -6]) == 0))

    negative = ("\n\nNegative elements: 6 " +
                str(counter_negative_dgts([-8, -6, -9, -4, -5, -6]) == 6))
    negative += ("\nNegative elements: 4 " +
                 str(counter_negative_dgts([-8, 6, 0, 9, -4, -5, -6, 0]) == 4))
    negative += ("\nNegative elements: 0 " +
                 str(counter_negative_dgts([8, 6, 0, 9, 4, 5, 6]) == 0))

    zero = ("\n\nZero elements: 3 " +
            str(counter_zero_dgts([0, 0, 0]) == 3))
    zero += ("\nZero elements: 4 " +
             str(counter_zero_dgts([-8, 6, 0, 9, -4, -5, -6, 0]) == 2))
    zero += ("\nZero elements: 0 " +
             str(counter_zero_dgts([8, 6, 9, 4, 5, 6]) == 0))

    print(extreme, average, positive, negative, zero)


if __name__ == '__main__':
    main()
    test()
