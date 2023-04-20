'''
Even/Odd Vector Values
v.1.0
Gerasimchik D.Y.
QA2022
20.04.2023
'''
from mn_task01 import create_list


def count_even_values(ls):
    count = 0

    for item in ls:
        if item % 2 == 0:
            count += 1

    return count


def count_odd_values(ls):
    count = 0

    for item in ls:
        if item % 2 != 0:
            count += 1

    return count


def main():
    size = int(input("Input size of list: "))
    ls = create_list(size)
    even = count_even_values(ls)
    odd = count_odd_values(ls)

    output(even, odd)


def output(ls):
    if ls:
        msg = "All elements are mirrored."
    else:
        msg = "The elements are NOT mirrored."
    print(msg)


def test():
    print(count_even_values([1, 2, 3, 4]) == 2)
    print(count_even_values([2, 4, 6, 8]) == 4)
    print(count_even_values([1, 3, 5, 7, 9]) == 0)


# пустой, с одним, с двумя

if __name__ == '__main__':
    test()
