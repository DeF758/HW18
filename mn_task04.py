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
    ls = create_list()
    even = count_even_values(ls)
    odd = count_odd_values(ls)
    output(even, odd)


def output(even, odd):
    print(f"Even: {even}, odd: {odd}.")


def test():
    even = str(count_even_values([1, 2, 3, 4]) == 2) + "\n"
    even += str(count_even_values([2, 4, 6, 8]) == 4) + "\n"
    even += str(count_even_values([1, 3, 5, 7, 9]) == 0) + "\n"
    even += str(count_even_values([]) == 0) + "\n"
    even += str(count_even_values([-2, 4, -6, 8]) == 4)

    odd = "\n\n" + str(count_odd_values([1, 2, 3, 4]) == 2) + "\n"
    odd += str(count_odd_values([2, 4, 6, 8]) == 0) + "\n"
    odd += str(count_odd_values([1, 3, 5, 7, 9]) == 5) + "\n"
    odd += str(count_odd_values([]) == 0) + "\n"
    odd += str(count_odd_values([-1, -3, 5, 7, -9]) == 5) + "\n"
    print(even, odd)


if __name__ == '__main__':
    main()
    test()
